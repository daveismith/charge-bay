import pcbnew
brd = pcbnew.GetBoard()
def move_items():
    fx = brd.FindFootprintByReference("D1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(126501100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D10")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137001100, 102628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D11")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137001100, 107878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D12")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137001100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D13")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(142251100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D14")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(142251100, 102628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D15")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(142251100, 107878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D16")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(142251100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D17")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(147501100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D18")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(147501100, 102628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D19")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(147501100, 107878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(126501100, 102628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D20")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(147501100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D21")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(186251100, 82878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D22")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(186251100, 88378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D23")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(186251100, 93628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(126501100, 107878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(126501100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(131751100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D6")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(131751100, 102628600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D7")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(131751100, 107878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D8")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(131751100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D9")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137001100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(127771100, 91378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(133021100, 91378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(138271100, 91378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(143521100, 91378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(148771100, 91378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(145173600, 77481100)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Q1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(116501100, 97378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Q2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(116501100, 101316100)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Q3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(116501100, 105253600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Q4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(116501100, 109191100)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Q5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(116501100, 113128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R6")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(118251100, 95478600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R7")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(118251100, 99428600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R8")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(118251100, 103378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R9")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(118251100, 107378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R10")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(118251100, 111378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(100009225, 74067975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R11")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(105486100, 76369850)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R12")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(105486100, 77798600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(152872975, 81211725)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(148785162, 70218288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(148785162, 68987975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137434537, 80497350)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(135886725, 72321725)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C6")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(137553600, 72321725)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R13")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(134537350, 72321725)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C7")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(133029225, 72321725)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("Y1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(154103287, 72877350)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C8")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(151444225, 71408913)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C9")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(156682975, 73036100)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U$1")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(131521100, 72480475)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U$2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(129616100, 72480475)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C10")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(104771725, 74067975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D24")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(148427975, 85418600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R14")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(149062975, 87164850)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(144459225, 68273600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R15")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(190536412, 82878600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R16")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(190536412, 88378600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R17")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(190536412, 93633913)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U$3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(164104537, 73393288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("RESET0")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(154357287, 75298288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U$4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(174820162, 73393288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C11")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(141800162, 70694538)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(123861412, 70456413)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-0.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C12")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(124615475, 68313288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C13")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(121519850, 70853288)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("D25")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(119575162, 72083600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(111836100, 137012350)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J2")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(163247287, 142647975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J3")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(123702662, 142647975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J4")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(185178600, 110128600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(170256100, 142647975)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J6")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(132791100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J7")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(136601100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J8")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(140411100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J9")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(144221100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J10")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(148031100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J11")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(151841100, 134694600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(90.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("J12")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(132537100, 81481600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("C14")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(127584100, 82116600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("R18")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(127584100, 80846600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(180.0, pcbnew.DEGREES_T))
    fx = brd.FindFootprintByReference("U$5")
    if fx is not None:
        fx.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(104851100, 93546600)))
        fx.SetOrientation(pcbnew.EDA_ANGLE(-90.0, pcbnew.DEGREES_T))
    pcbnew.Refresh()