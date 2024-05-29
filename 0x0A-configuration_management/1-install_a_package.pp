#!/usr/bin/puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}

package { 'werkzeug':
  ensure   => '2.0.3', # This version is compatible with Flask 2.1.0
  provider => 'pip3',
}
