/* Holistic Smile Design, Seitenskript. Jeder Block prüft, ob sein Element existiert. */
(function(){
  'use strict';
  var jahr=document.getElementById('jahr'); if(jahr) jahr.textContent=new Date().getFullYear();

  /* Erreichbarkeit: Mo bis Do 8 bis 18 Uhr, Fr 8 bis 15 Uhr (Europe/Berlin) */
  (function(){
    var el=document.getElementById('status'); if(!el)return;
    var ZEITEN={'Mo':[8,18],'Di':[8,18],'Mi':[8,18],'Do':[8,18],'Fr':[8,15]};
    function jetzt(){
      try{var f=new Intl.DateTimeFormat('de-DE',{timeZone:'Europe/Berlin',weekday:'short',hour:'numeric',minute:'numeric',hour12:false});
        var t={};f.formatToParts(new Date()).forEach(function(p){t[p.type]=p.value});
        return {tag:t.weekday.slice(0,2),std:+t.hour+(+t.minute)/60};}
      catch(e){var d=new Date();return {tag:['So','Mo','Di','Mi','Do','Fr','Sa'][d.getDay()],std:d.getHours()+d.getMinutes()/60};}
    }
    function setze(){
      var n=jetzt(), z=ZEITEN[n.tag], da=!!z&&n.std>=z[0]&&n.std<z[1], text;
      el.setAttribute('data-offen',da?'true':'false');
      if(da){text='Jetzt erreichbar';}
      else if(z&&n.std<z[0]){text='Heute ab 08:00 Uhr erreichbar';}
      else if(n.tag==='Fr'||n.tag==='Sa'||n.tag==='So'){text='Ab Montag 08:00 Uhr erreichbar';}
      else{text='Morgen ab 08:00 Uhr erreichbar';}
      el.textContent=text;
    }
    setze(); setInterval(setze,60000);
  })();

  /* Burger-Menü */
  var burger=document.querySelector('.burger'), nav=document.getElementById('hauptnav');
  if(burger&&nav){
  function schliesse(){burger.setAttribute('aria-expanded','false');burger.setAttribute('aria-label','Menü öffnen');nav.removeAttribute('data-offen');}
  burger.addEventListener('click',function(){
    var offen=burger.getAttribute('aria-expanded')==='true';
    if(offen){schliesse();}else{burger.setAttribute('aria-expanded','true');burger.setAttribute('aria-label','Menü schließen');nav.setAttribute('data-offen','true');}
  });
  nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',schliesse);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&burger.getAttribute('aria-expanded')==='true'){schliesse();burger.focus();}});
  }

  /* Anfahrtskarte erst nach Einwilligung */
  var box=document.getElementById('karte');
  if(box){
  var KARTE='https://www.google.com/maps?q=Oststra%C3%9Fe+120,+22844+Norderstedt&output=embed&hl=de';
  function ladeKarte(){
    if(box.getAttribute('data-geladen')==='true')return;
    var f=document.createElement('iframe');
    f.src=KARTE;f.title='Anfahrtskarte zu Holistic Smile Design, Oststraße 120, Norderstedt';f.loading='lazy';f.referrerPolicy='no-referrer-when-downgrade';f.allowFullscreen=true;
    box.appendChild(f);box.setAttribute('data-geladen','true');
  }
  function pruefeKarte(){
    if(window.aoEinwilligung&&window.aoEinwilligung.erlaubt('medien'))ladeKarte();
  }
  box.querySelector('[data-karte-laden]').addEventListener('click',function(){
    if(window.aoEinwilligung){window.aoEinwilligung.setze('medien',true);}
    ladeKarte();
  });
  document.addEventListener('ao:einwilligung',pruefeKarte);
  window.addEventListener('load',pruefeKarte);
  }

  /* Formular: Versand ueber anfrage-senden.php (PHP beim Hoster).
     Klappt der Versand nicht (z. B. auf der Vorschau ohne PHP), oeffnet sich das
     Mailprogramm mit der fertigen Anfrage. So geht keine Anfrage verloren.
     Pflichtfelder werden dreifach geprueft: im Browser, hier und im PHP-Skript. */
  var form=document.getElementById('formular');
  if(form){
  var ZIEL='info@holistic-smile-design.de';
  var zeit=form.querySelector('input[name="zeit"]'); if(zeit)zeit.value=String(Math.floor(Date.now()/1000));
  var knopf=form.querySelector('button[type="submit"]');
  function wert(n){var e=form.querySelector('[name="'+n+'"]');return e?e.value.trim():'';}
  function danke(ersatz){
    var p=form.querySelector('.danke .ersatzweg'); if(p)p.hidden=!ersatz;
    form.setAttribute('data-gesendet','true');
    var h=form.querySelector('.danke h3'); h.setAttribute('tabindex','-1'); h.focus();
  }
  function perMail(){
    var interessen=[].map.call(form.querySelectorAll('input[name="interesse[]"]:checked'),function(c){return c.value;}).join(', ');
    var text='Praxis: '+wert('praxis')+'\nAnsprechpartner: '+wert('name')+'\nTelefon: '+wert('telefon')+'\nE-Mail: '+wert('email')+'\nInteresse an: '+(interessen||'-')+'\n\n'+wert('nachricht');
    window.setTimeout(function(){location.href='mailto:'+ZIEL+'?subject='+encodeURIComponent('Anfrage über die Webseite: '+wert('praxis'))+'&body='+encodeURIComponent(text);},400);
  }
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var ok=true, erstes=null;
    form.querySelectorAll('.feld').forEach(function(feld){
      var inp=feld.querySelector('input,textarea'); if(!inp||!inp.required)return;
      var gueltig=inp.type==='checkbox'?inp.checked:(inp.type==='email'?/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(inp.value.trim()):inp.value.trim().length>1);
      feld.setAttribute('data-fehler',gueltig?'false':'true'); inp.setAttribute('aria-invalid',gueltig?'false':'true');
      if(!gueltig){ok=false; if(!erstes)erstes=inp;}
    });
    if(!ok){erstes.focus();return;}
    if(knopf)knopf.disabled=true;
    var fertig=function(){if(knopf)knopf.disabled=false;};
    if(!window.fetch||!window.FormData){fertig();danke(true);perMail();return;}
    fetch(form.getAttribute('action'),{method:'POST',body:new FormData(form),headers:{'Accept':'application/json'}})
      .then(function(r){return r.json();})
      .then(function(a){fertig(); if(a&&a.ok){danke(false);} else {throw new Error('Versand');}})
      ['catch'](function(){fertig();danke(true);perMail();});
  });
  form.querySelectorAll('input,textarea').forEach(function(inp){inp.addEventListener('input',function(){var f=inp.closest('.feld');if(f)f.setAttribute('data-fehler','false');});});
  }
})();
