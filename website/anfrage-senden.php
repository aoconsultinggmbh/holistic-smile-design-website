<?php
/* ============================================================================
   Kontaktformular Holistic Smile Design GmbH, Dentallabor Norderstedt.
   Nimmt die Anfrage vom Formular entgegen und schickt sie als E-Mail weiter.

   WAS HIER EINGESTELLT WIRD  (und sonst nichts):
     $an        Wer die Anfragen bekommt (abgestimmt mit Admir am 01.10.2026)
     $von       Absenderadresse. MUSS ein echtes Postfach auf derselben Domain
                sein, sonst stuft der Empfaenger die Mail als Spam ein.
                Zum Antworten zaehlt das Reply-To: dort steht die Praxis.

   SICHERHEIT
   - Honigtopf: ein fuer Menschen unsichtbares Feld. Fuellt es jemand aus,
     war es ein Roboter, und wir tun so, als waere alles gut.
   - Zeitsperre: wer das Formular in unter drei Sekunden absendet, ist keiner.
   - Alle Werte fuer den Mailkopf werden von Zeilenumbruechen befreit.
   - Es wird nichts gespeichert: keine Datenbank, keine Datei, kein Cookie.
   ============================================================================ */

$an  = 'info@holistic-smile-design.de';
$von = 'info@holistic-smile-design.de';

date_default_timezone_set('Europe/Berlin');
header('Content-Type: application/json; charset=utf-8');

function ende($ok, $text = '') {
  echo json_encode(array('ok' => $ok, 'text' => $text), JSON_UNESCAPED_UNICODE);
  exit;
}
function sauber($name) {
  $wert = isset($_POST[$name]) && !is_array($_POST[$name]) ? (string) $_POST[$name] : '';
  return mb_substr(trim($wert), 0, 3000);
}
function einzeilig($wert) {
  return trim(preg_replace('/[\r\n]+/', ' ', $wert));
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); ende(false, 'Nur POST.'); }

/* --- Roboterpruefung: stiller Erfolg, damit der Absender nichts lernt --- */
if (sauber('website') !== '') { ende(true); }
$start = (int) sauber('zeit');
if ($start > 0 && (time() - $start) < 3) { ende(true); }

/* --- Felder --- */
$praxis    = einzeilig(sauber('praxis'));
$name      = einzeilig(sauber('name'));
$email     = einzeilig(sauber('email'));
$telefon   = einzeilig(sauber('telefon'));
$nachricht = sauber('nachricht');
$interesse = array();
if (isset($_POST['interesse']) && is_array($_POST['interesse'])) {
  foreach ($_POST['interesse'] as $i) { $interesse[] = einzeilig(mb_substr((string) $i, 0, 80)); }
}
$datenschutz = sauber('datenschutz');

if ($praxis === '' || $name === '' || $telefon === '') { http_response_code(400); ende(false, 'Bitte füllen Sie die Pflichtfelder aus.'); }
if (!filter_var($email, FILTER_VALIDATE_EMAIL))         { http_response_code(400); ende(false, 'Bitte prüfen Sie die E-Mail-Adresse.'); }
if ($datenschutz === '')                                 { http_response_code(400); ende(false, 'Bitte stimmen Sie der Datenschutzerklärung zu.'); }

/* --- Mail bauen --- */
$betreff = 'Anfrage über die Webseite: ' . $praxis . ' - ' . $name;
$text  = "Anfrage über holistic-smile-design.de\n\n";
$text .= "Praxis:          $praxis\n";
$text .= "Ansprechpartner: $name\n";
$text .= "E-Mail:          $email\n";
$text .= "Telefon:         $telefon\n";
$text .= "Interesse an:    " . (count($interesse) ? implode(', ', $interesse) : '-') . "\n";
if ($nachricht !== '') { $text .= "\nNachricht:\n$nachricht\n"; }
$text .= "\n---\nGesendet am " . date('d.m.Y, H:i') . " Uhr. Datenschutzerklärung bestätigt.\n";
$text .= "Antworten Sie einfach auf diese Mail, das geht direkt an den Absender.\n";

$kopf  = 'From: Webseite Holistic Smile Design <' . $von . ">\r\n";
$kopf .= 'Reply-To: ' . $name . ' <' . $email . ">\r\n";
$kopf .= "MIME-Version: 1.0\r\n";
$kopf .= "Content-Type: text/plain; charset=UTF-8\r\n";
$kopf .= "Content-Transfer-Encoding: 8bit\r\n";

$betreff_kodiert = '=?UTF-8?B?' . base64_encode($betreff) . '?=';

if (@mail($an, $betreff_kodiert, $text, $kopf, '-f' . $von)) { ende(true); }
http_response_code(500);
ende(false, 'Die Anfrage konnte nicht verschickt werden. Bitte rufen Sie uns an: 040 94369370');
