# nethserver-danb35
This repo is the source for the RPM configuring the danb35 repository on a Nethserver system.  Although it may install on a CentOS 7 system, it is intended only for a Nethserver 7 system and may cause unintended operation elsewhere.

To install this repo, run `yum install https://repo.familybrown.org/nethserver/7/noarch/nethserver-danb35-1.0.0-6.ns7.noarch.rpm`.  You'll need this in order to use my other packages.  As of this writing, those include:

* [acme-dns](https://wiki.nethserver.org/doku.php?id=userguide:let_s_encrypt_acme-dns)
* [automx](https://wiki.nethserver.org/doku.php?id=email_autoconfig_module)
* [self-service-password](https://wiki.nethserver.org/doku.php?id=userguide:self-service-password)

Others may be added over time; consult the [Nethserver wiki](https://wiki.nethserver.org/doku.php?id=start) for documentation of any others.
