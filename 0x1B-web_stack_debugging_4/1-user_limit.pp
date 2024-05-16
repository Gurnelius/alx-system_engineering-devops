# Allow user holberton to login and open files with no error

# increase hard file limit for holberton
exec { 'increase-hard-file-limit-for-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# increase soft file limit for holberton
exec { 'increase-soft-file-limit-for-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
