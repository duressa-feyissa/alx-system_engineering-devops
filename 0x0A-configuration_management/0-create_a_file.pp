# creates a file in /tmp
# File path is /tmp/school
# File contains I love Puppet

file { '/tmp/school':
  content =>'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
