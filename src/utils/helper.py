class Helper:
    
    def ObjectSet(arr: list) -> list:
        seen = set()
        new_l = []
        for d in arr:
            t = tuple(d.items())
            if t not in seen:
                seen.add(t)
                new_l.append(d)
        return new_l

    def checkDomain(text: str) -> bool:
        if text[0] == '[' and text[-1] == ")":
            return True
        return False