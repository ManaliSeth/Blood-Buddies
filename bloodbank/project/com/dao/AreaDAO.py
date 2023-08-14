from project.com.dao import *


class AreaDAO:

    def adminInsertArea(self,areaVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "insert into AreaMaster(areaName,areaDescription,areaStatus) values ('" + areaVO.areaName + "','" + areaVO.areaDescription + "','" + areaVO.areaStatus + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def adminViewArea(self):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("Select * from AreaMaster where areaStatus='active'")
        viewArea = cursor.fetchall()
        return viewArea

    def adminDeleteArea(self,areaVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("update AreaMaster set areaStatus='deactive' where areaId = '" + areaVO.areaId + "'")
        connection.commit()
        cursor.close()
        connection.close()

    def adminEditArea(self,areaVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute("Select * from AreaMaster where areaId ={}".format(areaVO.areaId))
        editArea = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return editArea

    def adminUpdateArea(self,areaVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update AreaMaster set areaName = '" + areaVO.areaName + "', areaDescription= '" + areaVO.areaDescription + "' where areaId = '" + areaVO.areaId + "'")
        connection.commit()
        cursor.close()
        connection.close()

