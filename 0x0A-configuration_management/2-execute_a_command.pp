# kill the process killmenow
exec { 'killmenow_process':
	command => 'pkill -f killmenow',
	path =>['/usr/bin', '/usr/sbin']
}

