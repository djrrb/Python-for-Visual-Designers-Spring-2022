bp = BezierPath()
bp2 = BezierPath()
bp.moveTo((0, 0))
bp.lineTo((50, 100))
bp.lineTo((100, 0))

v = 10

for contour in bp:
    isMove = True
    for segment in contour:
        for point in segment:
            x, y = point
            x += randint(-v, v)
            y += randint(-v, v)
            if isMove:
                print('move', x, y)
                bp2.moveTo((x, y))
                isMove = False
            else:
                print('line', x, y)
                bp2.lineTo((x, y))

translate(200, 200)

drawPath(bp2)