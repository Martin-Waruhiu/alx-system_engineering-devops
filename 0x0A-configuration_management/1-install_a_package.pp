# puppet code to install flask using pip3

package {'Python-pip':
        ensure => installed
}

package {'flask':
        ensure => '2.1.0',
        provider => 'pip3',
        require => ['python3-pip']
}
