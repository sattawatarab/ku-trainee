@echo off
cd C:\OSGeo4W64\bin
ogr2ogr -f "PostgreSQL" -lco GEOMETRY_NAME=the_geom -lco FID=gid PG:"host=localhost user=postgres dbname=test password=P@ssw0rd" C:\Users\sattawat.a\Desktop\Python\TMD\tmd_today.vrt -nln tmd_data
ogr2ogr -f "csv" C:\Users\sattawat.a\Desktop\Python\TMD\output2bc.csv PG:"host=localhost user=postgres password=P@ssw0rd dbname=test" -sql "select * from ""tmd_data""" -lco ENCODING=UTF-8
exit
pause