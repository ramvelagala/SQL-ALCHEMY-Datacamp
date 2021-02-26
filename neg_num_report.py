for table_nm in table_items:
    df = sel_df(''' SELECT  
 
   attname       AS COL_NAME
FROM _v_table a
   JOIN _v_relation_column b
   ON a.objid   = b.objid
WHERE a.tablename = ''' + "'" + table_nm + "'" + '''
AND COL_NAME LIKE '%_SK'
AND a.schema = 'ADMIN'
ORDER BY attnum;
    ''')

    tcount = "SELECT COUNT(*) FROM " + table_nm
    total_count = sel_df(tcount)['COUNT'][0]

    for sk_col in df('COL_NAME'):
        select_stm = "SELECT count(*) from "+ table_nm +" where " +sk_col
        final_df = dat
