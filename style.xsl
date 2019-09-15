<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8"/>
  
  <xsl:template match="doc">
    <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html&gt;</xsl:text>
    <html>
      <head>
        <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>Vocabulaire</title>
	<style>
	  audio {
	  width: 80%
	  }
	</style>
	<script>
	  function PlaySound(soundobj) {
	  var thissound=document.getElementById(soundobj);
	  thissound.play();
	  }
	  
	  function StopSound(soundobj) {
	  var thissound=document.getElementById(soundobj);
	  thissound.pause();
	  thissound.currentTime = 0;
	  }
	  </script>
	</head>
      <body>
	<xsl:apply-templates/>
      </body>
    </html>
  </xsl:template>
  
  
  <xsl:template match="h1">
    <h1><xsl:apply-templates/></h1>
  </xsl:template>

    
  <xsl:template match="pl">
    <audio>
      <xsl:attribute name="id">
	<xsl:value-of select="@hash"/>
      </xsl:attribute>
      <xsl:attribute name="src">
	<xsl:text>gspeech/</xsl:text><xsl:value-of select="@hash"/><xsl:text>.mp3</xsl:text>
      </xsl:attribute>
    </audio>
    
    <p>
      <xsl:attribute name="onmouseover">
	<xsl:text>PlaySound('</xsl:text><xsl:value-of select="@hash"/><xsl:text>')</xsl:text>
      </xsl:attribute>
      <xsl:attribute name="onmouseout">
	<xsl:text>StopSound('</xsl:text><xsl:value-of select="@hash"/><xsl:text>')</xsl:text>
      </xsl:attribute>
      <xsl:value-of select="../@id[number(.) &gt; 0]"/><xsl:text> </xsl:text>
      <b><xsl:apply-templates/></b>
    </p>
  </xsl:template>
  
    <xsl:template match="ip">
    <p><xsl:apply-templates/></p>
  </xsl:template>

  <xsl:template match="fr">
    <p><i><xsl:apply-templates/></i></p>
    <hr/>
  </xsl:template>
  

</xsl:stylesheet> 
