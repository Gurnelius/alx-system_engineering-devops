# kill the process killmenow
exec { 'pkill':
	command =>  'pkill -f killmenow',
	path 	=>  ['/usr/bin', '/usr/sbin', '/bin'],
	onlyif  =>  'pgrep -f killmenow',
}
