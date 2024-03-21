class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate().lower())


class TrackableList(list):
    def append(self, obj):
        print("Append called")
        super().append(obj)


tl = TrackableList()
tl.append("1")
print(tl)
