from typing import List
import pyautogui
import numpy as np
import random
import cv2
from time import sleep


def choose(n, k):
    """A fast way to calculate binomial coefficients by Andrew Dalke (contrib)."""
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def bernstein_poly(i, n, t):
    """The Bernstein polynomial of n, i as a function of t."""
    return choose(n, i) * (t ** (n - i)) * (1 - t) ** i


def bezier_curve(points: List[tuple], nTimes: int = 1000):
    """
    Given a set of control points, return the bezier curve defined by the control points.

    points should be a list of lists, or list of tuples
    such as [ [1,1],
             [2,3],
             [4,5], ..[Xn, Yn] ]
    nTimes is the number of time steps, defaults to 1000
    See http://processingjs.nihongoresources.com/bezierinfo/
    """
    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])
    t = np.linspace(0.0, 1.0, nTimes)
    polynomial_array = np.array(
        [bernstein_poly(i, nPoints - 1, t) for i in range(0, nPoints)]
    )
    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)
    return list(zip(xvals, yvals))


class Mouse:
    def __init__(self):
        pyautogui.MINIMUM_DURATION = 0
        pyautogui.MINIMUM_SLEEP = 0
        self.endX = 0
        self.endY = 0

    def setCurrentPosition(self):
        self.currentX = pyautogui.position().x
        self.currentY = pyautogui.position().y

    def moveTo(self, x, y, wiggle=True):
        self.endX = x
        self.endY = y
        points = self.getPoints()
        if wiggle:
            for z in range(30):
                x = points[0][0]
                y = points[0][1]
                rand = random.randint(1, 4)
                if rand == 1:
                    points.insert(0, (x + 1, y + 1))
                elif rand == 2:
                    points.insert(0, (x + 1, y - 1))
                elif rand == 3:
                    points.insert(0, (x - 1, y + 1))
                elif rand == 4:
                    points.insert(0, (x - 1, y - 1))

        pyautogui.PAUSE = 0.5 / len(list(points))

        for x, y in reversed(points):
            pyautogui.moveTo(x, y)

    def moveToAndClick(
        self, x: int = None, y=None, wiggle=True, image=None, first=False
    ):
        if image is None:
            self.endX = x
            self.endY = y
        else:
            sleep(random.randint(1, 3))
            screenshot = cv2.cvtColor(
                np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR
            )
            screenshot2 = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            template = cv2.imread("templates/%s.png" % image, 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(screenshot2, template, cv2.TM_CCOEFF_NORMED)
            if first:
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if max_val > 0.8:
                    print(cv2.minMaxLoc(res))
                    clickSquare = [
                        (max_loc[0] + 5, max_loc[1] + 5),
                        (max_loc[0] + w - 5, max_loc[1] + h - 5),
                    ]
                    cv2.rectangle(
                        screenshot, clickSquare[0], clickSquare[1], (0, 255, 255), -1
                    )
                    x1, y1 = clickSquare[0]
                    x2, y2 = clickSquare[1]
                    x = random.randint(x1, x2)
                    y = random.randint(y1, y2)
                    cv2.circle(screenshot, (x, y), 1, (255, 0, 0))
                    cv2.imwrite("%s.png" % image, screenshot)
                    self.endX = x
                    self.endY = y
                else:
                    return
            else:
                threshold = 0.8
                if np.any(res >= threshold):
                    loc = np.where(res >= threshold)
                    for pt in zip(*loc[::-1]):
                        print(pt)
                        clickSquare = [
                            (pt[0] + 5, pt[1] + 5),
                            (pt[0] + w - 5, pt[1] + h - 5),
                        ]
                        cv2.rectangle(
                            screenshot,
                            clickSquare[0],
                            clickSquare[1],
                            (0, 255, 255),
                            -1,
                        )
                    x1, y1 = clickSquare[0]
                    x2, y2 = clickSquare[1]
                    x = random.randint(x1, x2)
                    y = random.randint(y1, y2)
                    cv2.circle(screenshot, (x, y), 1, (255, 0, 0))
                    cv2.imwrite("%s.png" % image, screenshot)
                    self.endX = x
                    self.endY = y
                else:
                    return

        points = self.getPoints()
        if wiggle:
            for z in range(25):
                x = points[0][0]
                y = points[0][1]
                rand = random.randint(1, 4)
                if rand == 1:
                    points.insert(0, (x + 1, y + 1))
                elif rand == 2:
                    points.insert(0, (x + 1, y - 1))
                elif rand == 3:
                    points.insert(0, (x - 1, y + 1))
                elif rand == 4:
                    points.insert(0, (x - 1, y - 1))

        pyautogui.PAUSE = 0.5 / len(list(points))

        for idx, (x, y) in enumerate(reversed(points)):
            if idx == len(points) - 1:
                pyautogui.click(x, y)
            else:
                pyautogui.moveTo(x, y)

    def getPoints(self):
        self.setCurrentPosition()
        if self.currentX <= self.endX:
            controlX = random.randint(self.currentX, self.endX)
        else:
            controlX = random.randint(self.endX, self.currentX)

        if self.currentY <= self.endY:
            controlY = random.randint(self.currentY, self.endY)
        else:
            controlY = random.randint(self.endY, self.currentY)

        return bezier_curve(
            [
                [self.currentX, self.currentY],
                [controlX, controlY],
                [self.endX, self.endY],
            ],
            nTimes=random.randint(200, 400),
        )
