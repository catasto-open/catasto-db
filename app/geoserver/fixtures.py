from datetime import datetime

from app.configs import cnf
from app.geoserver.api import (
    create_workspace,
    create_datastore,
    create_layer,
    get_settings,
    update_settings,
)

workspace = {
    "workspace": {
        "name": cnf.CATASTO_OPEN_GS_WORKSPACE,
        "namespace": {
            "prefix": "CatastoOpenDev",
            "uri": "catasto-open-dev",
            "isolated": False,
        },
    }
}

datastore = {
    "dataStore": {
        "name": cnf.CATASTO_OPEN_GS_DATASTORE,
        "description": cnf.CATASTO_OPEN_GS_DATASTORE,
        "type": "PostGIS",
        "enabled": True,
        "workspace": {
            "name": cnf.CATASTO_OPEN_GS_WORKSPACE,
            "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/rest/workspaces"
            f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
        },
        "connectionParameters": {
            "entry": [
                {"@key": "schema", "$": "public"},
                {"@key": "Evictor run periodicity", "$": "300"},
                {"@key": "Max open prepared statements", "$": "50"},
                {"@key": "encode functions", "$": "True"},
                {"@key": "Batch insert size", "$": "1"},
                {"@key": "preparedStatements", "$": "False"},
                {"@key": "database", "$": cnf.POSTGRES_DB},
                {
                    "@key": "host",
                    "$": f"{cnf.APP_CONFIG.COMPOSE_PROJECT_NAME}-db",
                },
                {"@key": "Loose bbox", "$": "True"},
                {"@key": "SSL mode", "$": "ALLOW"},
                {"@key": "Estimated extends", "$": "True"},
                {"@key": "fetch size", "$": "1000"},
                {"@key": "Expose primary keys", "$": "False"},
                {"@key": "validate connections", "$": "True"},
                {
                    "@key": "Support on the fly geometry simplification",
                    "$": "True",
                },
                {"@key": "Connection timeout", "$": "20"},
                {"@key": "create database", "$": "False"},
                {"@key": "Method used to simplify geometries", "$": "FAST"},
                {"@key": "port", "$": cnf.POSTGRES_CONTAINER_PORT},
                {"@key": "passwd", "$": cnf.POSTGRES_PASS},
                {"@key": "min connections", "$": "1"},
                {"@key": "dbtype", "$": "postgis"},
                {
                    "@key": "namespace",
                    "$": f"http://{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                },
                {"@key": "max connections", "$": "10"},
                {"@key": "Evictor tests per run", "$": "3"},
                {"@key": "Test while idle", "$": "True"},
                {"@key": "user", "$": cnf.POSTGRES_USER},
                {"@key": "Max connection idle time", "$": "300"},
            ]
        },
        "_default": True,
        "featureTypes": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
        f"/geoserver/rest/workspaces"
        f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
        f"/datastores/{cnf.CATASTO_OPEN_GS_DATASTORE}"
        f"/featuretypes.json",
    }
}

layers = [
    {
        "featureType": {
            "name": "catasto_comuni",
            "nativeName": "catasto_comuni",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_comuni",
            "keywords": {"string": ["features", "catasto_comuni"]},
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84 / '
                'Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n     '
                ' SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", '
                "NORTH], \n    "
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular '
                'Visualisation Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": -180.00000000000003,
                "maxx": 180.00000000000003,
                "miny": -85.06,
                "maxy": 85.06,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_comuni",
                        "sql": """select distinct c.comune as name,
                               c.codice as code from ctcn.comuni c
                               inner join ctmp.fogli f on
                               (c.codice = f.comune) where c.comune
                               ilike '%city%'||'%' group by
                               c.codice order by 1""",
                        "escapeSql": False,
                        "parameter": {
                            "name": "city",
                            "regexpValidator": "^[\\w\\d\\s]+$",
                        },
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "name",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "code",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_sezioni",
            "nativeName": "catasto_sezioni",
            "namespace": {
                "name": "CatastoOpenDev",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/namespaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_sezioni",
            "keywords": {"string": ["features", "catasto_sezioni"]},
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation Pseudo Mercator"], '
                '\n  PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": -8.9831528412e-6,
                "maxx": 0,
                "miny": -8.983152841e-6,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_sezioni",
                        "sql": """SELECT f.sezione as name
                               FROM  ctcn.comuni c
                               INNER JOIN ctmp.fogli f
                               ON (c.codice = f.comune)
                               where c.codice = '%cityCode%'
                               group by f.sezione order by 1""",
                        "escapeSql": False,
                        "parameter": {
                            "name": "cityCode",
                            "defaultValue": "H501",
                            "regexpValidator": "^[\\w\\d\\s]+$",
                        },
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": {
                    "name": "name",
                    "minOccurs": 1,
                    "maxOccurs": 1,
                    "nillable": False,
                    "binding": "java.lang.String",
                }
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_fogli",
            "nativeName": "catasto_fogli",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_fogli",
            "keywords": {"string": ["features", "catasto_fogli"]},
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n'
                '  GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1349515.7437343975,
                "maxx": 1431080.9594936338,
                "miny": 5109480.984138456,
                "maxy": 5182211.8792562885,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 12.122906187565325,
                "maxx": 12.85561898725561,
                "miny": 41.655279125617746,
                "maxy": 42.14158524854467,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_fogli",
                        "sql": """select cityCode,
                        section, sheet, number, geom,
                        st_envelope(geom) as extent
                        from (select f.foglio::integer as number,
                        f.comune as cityCode,
                        f.sezione as section,
                        f.foglio  as sheet,
                        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
                        as geom FROM ctmp.fogli f
                        where f.comune = '%cityCode%'
                        group by 1,2,3,4) as sheets
                        order by 1""",
                        "escapeSql": False,
                        "parameter": {
                            "name": "cityCode",
                            "defaultValue": "H501",
                            "regexpValidator": "^[\\w\\d\\s]+$",
                        },
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_fabbricati",
            "nativeName": "catasto_fabbricati",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_fabbricati",
            "keywords": {"string": ["features", "catasto_fabbricati"]},
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1388999.5654533699,
                "maxx": 1390217.763909564,
                "miny": 5154042.615019346,
                "maxy": 5155998.768255651,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 12.477595392821357,
                "maxx": 12.488538655744257,
                "miny": 41.95367438138326,
                "maxy": 41.966741399897344,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_fabbricati",
                        "sql": """select vf.codice as cityCode,
                        f.sezione as section,
                        vf.foglio as sheet,
                        vf.numero_f as number,
                        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
                        as geom,
                        st_envelope(st_transform(
                        st_setsrid(st_extent(f.geom),3004),3857))
                        as extent
                        from ctcn.v_fabbricati vf
                        right join ctmp.fabbricati f
                        on f.comune = vf.codice
                        and f.foglio = vf.foglio
                        and f.numero = vf.particella
                        where vf.codice = '%cityCode%'
                        and vf.foglio = '%citySheet%'
                        and vf.data_inizio<='%checkDate%'
                        and vf.data_fine_f>='%checkDate%' group by 1,2,3,4
                        order by 1,2,3,4""",
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "citySheet",
                                "defaultValue": 130,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "cityCode",
                                "defaultValue": "H501",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "checkDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_terreni",
            "nativeName": "catasto_terreni",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_terreni",
            "keywords": {"string": ["features", "catasto_terreni"]},
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1390118.7682350094,
                "maxx": 1391947.0149667438,
                "miny": 5154907.727144444,
                "maxy": 5156456.696837757,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 12.487649362469117,
                "maxx": 12.504072782291702,
                "miny": 41.95945362321631,
                "maxy": 41.9697999558413,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_terreni",
                        "sql": """select vt.codice as cityCode,
                        p.sezione as section,
                        vt.foglio as sheet,
                        vt.numero_f as number,
                        st_transform(st_setsrid(
                        st_extent(p.geom),3004),3857) as geom,
                        st_envelope(st_transform(
                        st_setsrid(st_extent(p.geom),3004),3857))
                        as extent
                        from ctcn.v_terreni vt
                        right join ctmp.particelle p
                        on p.comune = vt.codice
                        and p.foglio = vt.foglio::text
                        and p.numero = vt.particella
                        where vt.codice = '%cityCode%'
                        and vt.foglio::text = '%citySheet%'
                        and vt.data_inizio<='%checkDate%'
                        and vt.data_fine_f>='%checkDate%'
                        group by 1,2,3,4
                        order by 1,2,3,4""",
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "citySheet",
                                "defaultValue": 130,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "cityCode",
                                "defaultValue": "H501",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "checkDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_persone_fisiche",
            "nativeName": "catasto_persone_fisiche",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_persone_fisiche",
            "keywords": {"string": ["features", "catasto_persone_fisiche"]},
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_persone_fisiche",
                        "sql": """select distinct
                    string_agg(f.soggetto::text, ',') as subjects,
                    f.tipo_sog as subjectType,
                    f.nome as firstName,
                    f.cognome as lastName,
                    f.codfiscale AS fiscalCode,
                    CASE
                    WHEN length(f.data) = 8 THEN to_date(f.data, 'DDMMYYYY')
                    END AS dateOfBirth,
                    c.comune || CASE
                    WHEN c.provincia <> '' THEN (' (' || c.provincia) || ')'
                    ELSE '' END AS cityOfBirth,
                    CASE f.sesso
                    WHEN '2' THEN 'Femmina'
                    ELSE 'Maschio'
                    END AS gender
                    FROM ctcn.ctfisica f
                    LEFT JOIN ctcn.comuni c
                    ON c.codice = f.luogo
                    where (f.codfiscale ilike %fiscalCode%)
                    or (f.cognome ilike %lastName%
                    and f.nome ilike %firstName%)
                    group by f.tipo_sog,
                    f.nome, f.cognome,
                    f.codfiscale,
                    dateOfBirth, cityOfBirth, gender""",
                        "escapeSql": False,
                        "parameter": [
                            {"name": "lastName", "defaultValue": "null"},
                            {"name": "firstName", "defaultValue": "null"},
                            {"name": "fiscalCode", "defaultValue": "null"},
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subjects",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subjecttype",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "firstname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lastname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "fiscalcode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "dateofbirth",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "cityofbirth",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "gender",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_persone_giuridiche",
            "nativeName": "catasto_persone_giuridiche",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_persone_giuridiche",
            "keywords": {"string": ["features", "catasto_persone_giuridiche"]},
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n   '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_persone_giuridiche",
                        "sql": """select distinct
                        f.soggetto::text as subjects,
                        f.tipo_sog as subjectType,
                        f.denominaz as businessName,
                        f.codfiscale as vatNumber,
                        (select c.comune
                        from ctcn.comuni c where c.codice = f.sede)
                        as branch
                        FROM ctcn.ctnonfis f
                        where (f.codfiscale like %vatNumber%)
                        or (f.denominaz  ilike %businessName% || '%')""",
                        "escapeSql": False,
                        "parameter": [
                            {"name": "businessName", "defaultValue": "null"},
                            {"name": "vatNumber", "defaultValue": "null"},
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subjects",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subjecttype",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "businessname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "vatnumber",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "branch",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_particelle_soggetto",
            "nativeName": "catasto_particelle_soggetto",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_particelle_soggetto",
            "keywords": {
                "string": ["features", "catasto_particelle_soggetto"]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84 / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1409699.6261978347,
                "maxx": 1409720.3750075395,
                "miny": 5130138.539788292,
                "maxy": 5130201.600410742,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 12.663547202310912,
                "maxx": 12.663733592039762,
                "miny": 41.79377980789061,
                "maxy": 41.79420214712485,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_particelle_soggetto",
                        "sql": """(select buildings.cityCode,
                        buildings.section,  buildings.sheet,
                        buildings.number,
                        st_transform(
                        st_setsrid(ST_Envelope(buildings.geom),3004),3857)
                         as geom, st_envelope(st_transform(
                        st_setsrid(ST_Envelope(buildings.geom),3004),3857))
                         as extent,
                        vsf.ubicazione as city, vsf.subalterno as subordinate,
                        vsf.titolo as right, vsf.quota as part,
                        vsf.classamento as classification,
                        vsf.classe as class,
                        vsf.consistenza as consistency,
                        vsf.rendita as income,
                        vsf.partita as lot,
                        vsf.tipo_immobile as propertyType
                        from (select f.comune  as cityCode,
                        f.sezione  as section,
                        f.foglio  as sheet,
                        f.numero as number,
                        f.geom from ctmp.fabbricati f) as buildings
                        right join ctcn.v_soggetti_fabbricati
                        vsf on  buildings.number = vsf.particella and
                        buildings.cityCode = vsf.codice and
                        buildings.sheet = vsf.foglio
                        where vsf.soggetto in (%subjects%)
                        and vsf.tipo_sog='%subjectType%')
                        union (select  lands.cityCode,
                        lands.section,
                        lands.sheet,
                        lands.number,
                        st_transform(
                        st_setsrid(ST_Envelope(lands.geom),3004),3857) as geom,
                        st_envelope(st_transform(
                        st_setsrid(ST_Envelope(lands.geom),3004),3857))
                        as extent, vst.ubicazione as city,
                        vst.subalterno as subordinate,
                        vst.titolo as right,
                        vst.quota as part,
                        vst.classamento as classification,
                        vst.classe as class,
                        vst.consistenza as consistency,
                        vst.rendita as income,
                        vst.partita as lot,
                        vst.tipo_immobile as propertyType
                        from (select p.comune as cityCode,
                        p.sezione  as section,
                        p.foglio  as sheet,
                        p.numero as number,
                        p.geom from ctmp.particelle p) as lands
                        inner join ctcn.v_soggetti_terreni
                        vst on lands.number = vst.particella
                        and lands.cityCode = vst.codice and
                        lands.sheet = vst.foglio
                        where vst.soggetto in (%subjects%)
                        and vst.tipo_sog='%subjectType%')
                        order by 1,2,3,4""",
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "subjects",
                                "defaultValue": "1535337,2653458",
                                "regexpValidator": "^([0-9]+,)*[0-9]+$",
                            },
                            {
                                "name": "subjectType",
                                "defaultValue": "P",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                    {
                        "name": "city",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "right",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "part",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "classification",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "consistency",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "income",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_titolari_immobile",
            "nativeName": "catasto_titolari_immobile",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_titolari_immobile",
            "keywords": {"string": ["features", "catasto_titolari_immobile"]},
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_titolari_immobile",
                        "sql": """select vipg.nominativo as nominative,
                        vipg.codice_fiscale as fiscalCode,
                        vipg.comune_sede as city,
                        vipg.titolo as right,
                        vipg.quota as part
                        from ctcn.v_immobili_pg vipg
                        where vipg.immobile=%property%
                        and vipg.tipo_imm='%propertyType%'
                        and vipg.codice='%cityCode%'
                        and vipg.data_inizio::text<='%checkDate%'
                        and vipg.data_fine_f::text>='%checkDate%'
                        union
                        select vipf.nominativo as nominative,
                        vipf.codice_fiscale as fiscalCode,
                        vipf.comune_nascita as city,
                        vipf.titolo as right,
                        vipf.quota as part
                        from ctcn.v_immobili_pf
                        vipf where vipf.immobile=%property%
                        and vipf.codice='%cityCode%'
                        and vipf.tipo_imm='%propertyType%'
                        and vipf.data_inizio::text<='%checkDate%'
                        and vipf.data_fine_f::text>='%checkDate%'""",
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H501",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "propertyType",
                                "defaultValue": "F",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "property",
                                "defaultValue": 1383488,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "checkDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "nominative",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "fiscalcode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "city",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "right",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "part",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_dettagli_terreno",
            "nativeName": "catasto_dettagli_terreno",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_dettagli_terreno",
            "keywords": {"string": ["features", "catasto_dettagli_terreno"]},
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_dettagli_terreno",
                        "sql": """select vt.immobile as property,
                        vt.tipo_imm as propertyType,
                        vt.subalterno as subordinate,
                        vt.qualita  as quality,
                        vt.classe as class,
                        vt.ettari as hectares,
                        vt.are, vt.centiare,
                        vt.partita as lot,
                        vt.reddito_dominicale as cadastralRent,
                        vt.reddito_agrario as agriculturalRent
                        from ctcn.v_terreni vt
                        where vt.codice = '%cityCode%'
                        and  vt.foglio = '%citySheet%'
                        and vt.numero_f = '%landNumber%'
                        and  vt.data_inizio::text<='%checkDate%'
                        and vt.data_fine_f::text>='%checkDate%'""",
                        "escapeSql": True,
                        "parameter": [
                            {
                                "name": "landNumber",
                                "defaultValue": "00005",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "citySheet",
                                "defaultValue": 131,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "cityCode",
                                "defaultValue": "H501",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "checkDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": True,
            "simpleConversionEnabled": True,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": True,
            "forcedDecimal": True,
            "overridingServiceSRS": True,
            "skipNumberMatched": True,
            "circularArcPresent": True,
            "attributes": {
                "attribute": [
                    {
                        "name": "property",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Long",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "quality",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "hectares",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "are",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "centiare",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "cadastralrent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "agriculturalrent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": "catasto_dettagli_fabbricato",
            "nativeName": "catasto_dettagli_fabbricato",
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": "catasto_dettagli_fabbricato",
            "keywords": {
                "string": ["features", "catasto_dettagli_fabbricato"]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": "catasto_dettagli_fabbricato",
                        "sql": """select vf.subalterno as subordinate,
                        vf.immobile as property,
                        vf.tipo_imm as propertyType,
                        vf.zona_censuaria as censusZone,
                        vf.categoria as category,
                        vf.classe as _class,
                        vf.consistenza as consistency,
                        vf.rendita as rent,
                        vf.partita as lot
                        from ctcn.v_fabbricati vf
                        where vf.codice = '%cityCode%'
                        and vf.foglio = '%citySheet%'
                        and vf.numero_f = '%buildingNumber%'
                        and vf.data_inizio::text<='%checkDate%'
                        and vf.data_fine_f::text>='%checkDate%'""",
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "citySheet",
                                "defaultValue": 131,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "cityCode",
                                "defaultValue": "H501",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "buildingNumber",
                                "defaultValue": "00013",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "checkDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "property",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Long",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "censuszone",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "category",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "_class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "consistency",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "rent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
]


def load_workspaces():
    create_workspace(workspace)


def load_data_stores():
    create_datastore(datastore)


def load_layers():
    for layer in layers:
        create_layer(layer)


def load_settings():
    settings = get_settings()
    settings["global"]["settings"]["numDecimals"] = 8
    update_settings(settings)
