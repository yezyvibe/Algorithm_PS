def solution(w, h):
    def getGcd(w,h):
        if (h == 0):
            return w
        return getGcd(h, w % h)

    return w * h - (w + h - getGcd(w, h))