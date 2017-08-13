#!/usr/bin/env python3


s1 = '''
asm     else    new     this
auto    enum    operator    throw
bool    explicit    private     true
break   export  protected   try
case    extern  public  typedef
catch   false   register    typeid
char    float   reinterpret_cast    typename
class   for     return  union
const   friend  short   unsigned
const_cast  goto    signed  using
continue    if  sizeof  virtual
default     inline  static  void
delete  int     static_cast     volatile
do  long    struct  wchar_t
double  mutable     switch  while
dynamic_cast    namespace   template     '''


# [print(x) for x in sorted(s1.split())]

# import subprocess

# lscmd = 'aws s3 ls s3://flight.pq.11'
# ret = subprocess.run(lscmd.split(' '), stdout=subprocess.PIPE)
# [print(x) for x in map(lambda x: x.strip().split(' ')[1].split('/')[0], ret.stdout.decode().splitlines())]

import os
import django
from django.template import Context, Template


def test_template():
    t = Template("My name is {{ person.first_name }}.")
    d = {"person": {"first_name": "Joe", "last_name": "Johnson"}}
    print(t.render(Context(d)))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    test_template()
