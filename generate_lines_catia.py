import win32com.client

def generate_points_catia(transfered_coord):
    gauge_length = float(input("--------------------\n--------------------\nInput the GL:"))
    ball_radius = float(input("--------------------\nInput the Ball nose Radius (A1):"))

    CATIA = win32com.client.Dispatch('catia.application')
    oPart = CATIA.Documents.Item("Toolpath.CATPart").Part
    myPBody = oPart.HybridBodies.Add()
    ref_body = oPart.CreateReferenceFromObject(myPBody)
    oPart.HybridShapeFactory.ChangeFeatureName(ref_body, "GeometryFromNC")

    #AxisSystem = oPart.AxisSystems.Item("alignment")

    for i in transfered_coord:
        #print(i)
        x, y, z, di, dj, dk, = i[1:7]

        correct_length = gauge_length - ball_radius

        tip_x = x - correct_length * di
        tip_y = y - correct_length * dj
        tip_z = z - correct_length * dk
        Point = oPart.HybridShapeFactory.\
                        AddNewPointCoord(tip_x * 25.4, tip_y * 25.4, tip_z * 25.4)
        #Point.RefAxisSystem = oPart.CreateReferenceFromObject(AxisSystem)

        myPBody.AppendHybridShape(Point)

        ref_line = oPart.CreateReferenceFromObject(Point)

        oPart.HybridShapeFactory.ChangeFeatureName(ref_line, i[0])


    oPart.Update()


def generate_lines_catia(transfered_coord):
    gauge_length = float(input("--------------------\n--------------------\nInput the GL:"))
    ball_radius = float(input("--------------------\nInput the Ball nose Radius (A1):"))

    CATIA = win32com.client.Dispatch('catia.application')
    oPart = CATIA.Documents.Item("Toolpath.CATPart").Part
    myPBody = oPart.HybridBodies.Add()
    ref_body = oPart.CreateReferenceFromObject(myPBody)
    oPart.HybridShapeFactory.ChangeFeatureName(ref_body, "GeometryFromNC")

    #AxisSystem = oPart.AxisSystems.Item("alignment")

    for i in transfered_coord:
        #print(i)
        x, y, z, di, dj, dk, = i[1:7]

        correct_length = gauge_length - ball_radius

        tip_x = x - correct_length * di
        tip_y = y - correct_length * dj
        tip_z = z - correct_length * dk
        Point = oPart.HybridShapeFactory.\
                        AddNewPointCoord(tip_x * 25.4, tip_y * 25.4, tip_z * 25.4)
        #Point.RefAxisSystem = oPart.CreateReferenceFromObject(AxisSystem)

        Dir = oPart.HybridShapeFactory.AddNewDirectionByCoord(di, dj, dk)
        #Dir.RefAxisSystem = oPart.CreateReferenceFromObject(AxisSystem)

        Line = oPart.HybridShapeFactory.AddNewLinePtDir(Point, Dir, 0, correct_length * 25.4, False)

        myPBody.AppendHybridShape(Line)

        ref_line = oPart.CreateReferenceFromObject(Line)

        oPart.HybridShapeFactory.ChangeFeatureName(ref_line, i[0])

    oPart.Update()
