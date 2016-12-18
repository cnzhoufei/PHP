<?php



function wp_is_mobile() {
 static $is_mobile = null;
  
 if ( isset( $is_mobile ) ) {
  return $is_mobile;
 }
  
 if ( empty($_SERVER['HTTP_USER_AGENT']) ) {
  $is_mobile = false;
 } elseif ( strpos($_SERVER['HTTP_USER_AGENT'], 'Mobile') !== false 
  || strpos($_SERVER['HTTP_USER_AGENT'], 'Android') !== false
  || strpos($_SERVER['HTTP_USER_AGENT'], 'Silk/') !== false
  || strpos($_SERVER['HTTP_USER_AGENT'], 'Kindle') !== false
  || strpos($_SERVER['HTTP_USER_AGENT'], 'BlackBerry') !== false
  || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mini') !== false
  || strpos($_SERVER['HTTP_USER_AGENT'], 'Opera Mobi') !== false ) {
   $is_mobile = true;
 } else {
  $is_mobile = false;
 }
  
 return $is_mobile;
}