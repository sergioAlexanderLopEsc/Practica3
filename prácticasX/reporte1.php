<?php
    require('../../controlador/fpdf186/fpdf.php');

    $pdf = new FPDF();
    $pdf->AddPage();
    $pdf->SetFont('Arial','B',16);
    $cadena1 = "i";
    $cadena2 = mb_convert_encoding($cadena1,'UTF-16','UTF-8');
    $cadena3 = ltrim($cadena2);
    $cadena4 = "e";
    $cadena5 = mb_convert_encoding($cadena4,'UTF-16','UTF-8');
    $cadena6 = ltrim($cadena5);
    $pdf->Cell(40,10,$cadena3.'Viva M'. $cadena6. 'xico!');
    $pdf->Output();
?>  