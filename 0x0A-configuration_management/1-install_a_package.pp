# install a specific version of flask
#!/usr/bin/puppet
package{'flask':
ensure   => '2.1.0',
provider => 'pip3'
}
