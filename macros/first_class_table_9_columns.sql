{% macro nine_columns(table1, column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8, column_9 ) %}

select {{ column_1 }}, {{ column_2 }}, {{ column_3 }}, {{ column_4 }}, {{ column_5 }}, {{ column_6 }}, {{ column_7 }}, {{ column_8 }}, {{ column_9 }} from {{ table1 }}

{% endmacro %}
