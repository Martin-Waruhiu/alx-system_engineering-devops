# puppet code to kill a process in shell

exec { 'killmenow':

	command => 'pkill killmenow',
	provider => 'shell'
	onlyif => 'pgrep killmenow',
}
