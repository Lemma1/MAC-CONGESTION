import logging

class Router(object):
    def db_for_read(self, model, **hints):
        logging.warning("read")
        database = getattr(model, "_DATABASE", None)
        if database:
            return database
        else:
            return "default"

    def db_for_write(self, model, **hints):
        logging.warning("write")

        # CHANGE!!!!
        # return 'psql'

        database = getattr(model, "_DATABASE", None)
        # logging.warning(model)
        # logging.warning(database)
        if database:
            return database
        else:
            return "default"

    def allow_relation(self, obj1, obj2, **hints):
        # CHANFE!
        return True
        # logging.warning("relation")
        db_list = ['default', 'psql']
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        else:
            return False

    def allow_migrate(self, db, app_label, model_name = None, **hints):

        # logging.warning("check allow----")
        # logging.warning(app_label)
        # logging.warning(model_name)
        # logging.warning(db)



        if (model_name in ["link", "philly_link", "philly_request", "philly_congestion", "philly_congestion_array", "philly_dms",
                           "philly_congestion_array_online", "philly_online_loading"] or getattr(hints["model"], "_DATABASE", None) == "psql"):
            if (db == "psql"):
                return True;
            else:
                return False;
        else:
            if (db == "default"):
                return True;
            else:
                return False;

        # # if (app_label == "traffic" and getattr(hints["model"], "_DATABASE", None) == "psql" and db == "psql"):
        # #     logging.warning("YES, link into psql");
        # #     return True;
        # # if (app_label == "traffic" and getattr(hints["model"], "_DATABASE", None) == None and db == "default"):
        # #     return True;
        # # if (app_label != "traffic" and db == "default"):
        # #     return True;
        # # # logging.warning("FFFF");
        # # return False;




        # if (model_name == "link" and db == "psql"):
        #     return True;
        # if (getattr(hints["model"], "_DATABASE", None) == None and db == "default"):
        #     return True;
        # return False;

        # # if (db == "psql" and app_label != "traffic"):
        # #     # some hints doesn't have model field, this clouse prevents warning
        # #     # Assuming psql only holds models in traffic app
        # #     return False;
        # # logging.warning(getattr(hints["model"], "_DATABASE", None))
        # # if ((getattr(hints["model"], "_DATABASE", None) == None and db == "default")
        # #     or (getattr(hints["model"], "_DATABASE", None) == "psql" and db == "psql")):
        # #     logging.warning("T")
        # #     return True
        # # else:
        # #     # logging.warning("F")
        # #     return False
        # # if (logging.warning(getattr(hints["model"], "_DATABASE", None)) == "psql" and db == "psql") or \
        # #     (logging.warning(getattr(hints["model"], "_DATABASE", None)) != None and db != "default"):
        # #     logging.warning("true");
        # #     return True
        # # else:
        # #     logging.warning("false");
        # #     return False
