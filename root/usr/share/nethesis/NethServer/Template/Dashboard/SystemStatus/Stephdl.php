<?php

echo "<div class='dashboard-item'>";
echo "<dl>";
echo $view->header()->setAttribute('template',$T('Stephdl_Title'));
echo "<dt>".$T('NethserverID_label')."</dt><dd>"; echo $view->textLabel('uuid'); echo "</dd>";
echo "<dt>".$T('StephdlOnline_label')."</dt><dd>";
$online = $T('Online_label');
$offline = $T('Offline_label');

       ini_set("default_socket_timeout","05");
       set_time_limit(5);
       $f=fopen("http://mirror.de-labrusse.fr","r");
       $r=fread($f,1000);
       fclose($f);
       if(strlen($r)>1) {
       echo("<span class='green'>$online</span>");
       }
       else {
       echo("<span class='red'>$offline</span>");
       }

echo "</dl>";
echo "</div>";

