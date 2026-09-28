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

  /* Formular: Entwurf, verschickt nichts */
  var form=document.getElementById('formular');
  if(form){
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
    /* HIER beim Livegang: Daten per fetch() an den Server schicken und erst bei Erfolg die Danke-Ansicht zeigen. */
    form.setAttribute('data-gesendet','true');
    form.querySelector('.danke h3').setAttribute('tabindex','-1');
    form.querySelector('.danke h3').focus();
  });
  form.querySelectorAll('input,textarea').forEach(function(inp){inp.addEventListener('input',function(){var f=inp.closest('.feld');if(f)f.setAttribute('data-fehler','false');});});
  }
})();
