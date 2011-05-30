#####################
Initial Configuration
#####################


How Pyramid Project was originally created
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   pip install pyramid
   pip install pyramid_jinja2
   pip install pyramid_beaker

::

   paster create -t pyramid_routesalchemy
   Project Name: pythonla

   cd pythonla 
   mv * .* ../


How Pyramid was configured to use Pyramid Jinja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__init__.py
::

    config.include('pyramid_jinja2')

How Pyramid was configured to use Beaker Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__init__.py
~~~~~~~~~~~
::

    from pyramid_beaker import session_factory_from_settings
    session_factory = session_factory_from_settings(settings)

development.ini
~~~~~~~~~~~~~~~
::

    session.type = file
    session.data_dir = %(here)s/data/sessions/data
    session.lock_dir = %(here)s/data/sessions/lock
    session.key = mykey
    session.secret = mysecret
    session.cookie_on_exception = true

How Pyramid was configured to use Beaker Cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__init__.py
~~~~~~~~~~~
::

    from pyramid_beaker import set_cache_regions_from_settings 
    set_cache_regions_from_settings(settings)

development.ini
~~~~~~~~~~~~~~~

::

    cache.regions = default_term, second, short_term, long_term
    cache.type = memory
    cache.second.expire = 1
    cache.short_term.expire = 60
    cache.default_term.expire = 300 
    cache.long_term.expire = 3600

