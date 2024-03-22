# Install flask and Werkzeug

# ensure that python is installed
package { 'python3.8':
  ensure => present,
}

# ensure pip is installed
package { 'python3-pip':
  ensure => present,
}

# Install Flask 2.1.0 
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
