<?php
/**
 * 获取php.exe的路径
 */
function php_path() {   
        $php_path='';    
        if ($php_path != '') {           
            return $php_path;      
        }
        if (substr(strtolower(PHP_OS), 0, 3) == 'win') {           
            $ini = ini_get_all();                    
            $path = $ini['extension_dir']['local_value'];           
            $php_path = str_replace('\\', '/', $path);           
            $php_path = str_replace(array('/ext/', '/ext'), array('/', '/'), $php_path);           
            $real_path = $php_path . 'php.exe';       
        } else {           
            $real_path = PHP_BINDIR . '/php';       
        }
        if (strpos($real_path, 'ephp.exe') !== FALSE) {           
            $real_path = str_replace('ephp.exe', 'php.exe', $real_path);  
        }       
        $php_path = $real_path;       
        return $php_path;   
    }