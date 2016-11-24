from __future__ import unicode_literals
from django.db import models as m

headers = ["Maecenas mauris","Justo elementum","Quis euismod","Efficitur rhoncus","In metus","Phasellus vel","Nisi tellus"]
contents = ["Donec feugiat nisi non purus scelerisque cursus. Fusce vitae dolor metus. Etiam nec lacus sapien. Morbi in leo"
            " sit amet neque blandit pharetra. Pellentesque vel gravida felis, ac elementum mi. Aliquam scelerisque, erat in "
            "Duis lacinia, metus nec blandit iaculis, enim libero imperdiet",
            "tempus rhoncus, nisl elit vehicula arcu, quis ornare magna orci quis quam. Sed at nulla lectus. Maecenas suscipit"
            " et erat nec feugiat. In ac nisi vel orci congue mattis. Suspendisse pharetra, leo nec varius efficitur, ex mi"
            " commodo urna, ut accumsan justo nisi non lacus. ",
            " ex, quis laoreet felis dui ac purus. Ut a magna id risus feugiat laoreet. Aliquam erat volutpat. Lorem ipsum dolor"
            " sit amet, consectetur adipiscing elit.",
            "Fusce elementum ante ut ante posuere, in semper enim tincidunt. Curabitur tempus nisi id purus bibendum semper. "
            "Aliquam sit amet ligula luctus, pharetra nulla id, ultricies lectus. Sed nec lobortis neque, sit amet gravida ex. ",
            "Maecenas in elit purus. In aliquet maximus neque eu vestibulum. Proin venenatis fringilla ex, vel faucibus orci "
            "aliquet id. Mauris viverra elit in orci placerat vestibulum. Curabitur porttitor congue mi.",
            "Nunc porttitor, augue vitae cursus volutpat, sapien sem lobortis ligula, ac mattis neque nisl id elit. Quisque vel"
            " nulla tempus mauris faucibus posuere. Curabitur a ligula orci. Vestibulum rhoncus augue imperdiet tincidunt iaculis."
            " Pellentesque sagittis ultrices diam eu consequat.",
            "Donec enim risus, sollicitudin sed lorem eu, ullamcorper tincidunt"
            " est. Vivamus vitae malesuada massa. In pharetra sapien augue, sit amet luctus lorem pellentesque sed."]
list=[]
for i in range(0, len(headers)):
    list.append((headers[i],contents[i]))
print list
