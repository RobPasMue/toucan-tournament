.. _ref_api_reference:

API reference
=============

This page contains the ``toucan-mvp-calculator`` API reference.

.. toctree::
   :titlesonly:

   {% for page in pages %}
   {% if (page.top_level_object or page.name.split('.') | length == 3) and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}
