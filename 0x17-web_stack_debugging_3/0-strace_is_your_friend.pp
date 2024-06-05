# puppet fix for Apache server returning 500 error

exec { 'wordpress site fix':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
