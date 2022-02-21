import win32com.client

def generate_lines_catia(transfered_coord):
    gauge_length = float(input("--------------------\n--------------------\nInput the GL:"))

    CATIA = win32com.client.Dispatch('catia.application')
    oPart = CATIA.ActiveDocument.part
    myPBody = oPart.HybridBodies.Add()
    ref_body = oPart.CreateReferenceFromObject(myPBody)
    oPart.HybridShapeFactory.ChangeFeatureName(ref_body, "GeometryFromNC")

    for i in transfered_coord:
        x, y, z, di, dj, dk, = i[1:7]
        tip_x = x - gauge_length * di
        tip_y = y - gauge_length * dj
        tip_z = z - gauge_length * dk
        Point = oPart.HybridShapeFactory.\
                        AddNewPointCoord(tip_x * 25.4, tip_y * 25.4, tip_z * 25.4)

        Dir = oPart.HybridShapeFactory.\
                    AddNewDirectionByCoord(di, dj, dk)


        Line = oPart.HybridShapeFactory.\
                   AddNewLinePtDir(Point, Dir, 0, 3 * 25.4, False)

        myPBody.AppendHybridShape(Line)

        ref_line = oPart.CreateReferenceFromObject(Line)
        oPart.HybridShapeFactory.ChangeFeatureName(ref_line, i[0])


    oPart.Update()
