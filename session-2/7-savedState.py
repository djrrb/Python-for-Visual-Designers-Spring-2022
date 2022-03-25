# save our original state
# everything without indent will be drawn black from the bottom left
with savedState():
    # move to the center
    # make a green circle
    fill(0, 1, 0)
    translate(width()/2, height()/2)
    oval(0, 0, 100, 100)

    # save our state again
    with savedState():
        # draw a rect rectangle rotated 45 degrees (so a diamond)
        rotate(45)
        fill(1, 0, 0)
        rect(0, 0, 100, 100)
    # when we dedent, we go back to drawing green from the center
    font('Helvetica', 200)
    text('hello world', (100, 0))
# dedent again, and we are drawing from the bottom left
fontSize(100)
text('hello world', (0, 0))