#Your SSH client configuration must be configured to use the private key ~/.ssh/school
#Your SSH client configuration must be configured to refuse to authenticate using a password

file_line { 'Turn off password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentitiyFile ~/.ssh/school',
}