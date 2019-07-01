# *_*coding:utf-8 *_*
import hou
import os
import json
import toolutils
jsonPath = os.path.dirname(__file__)
with open("%s/dir.json"%jsonPath) as file:
    dict_all = json.loads(file.read())

obj=hou.node("/obj")
#创建摄像机并导入摄像机数据
camera_alembic=obj.createNode("alembicarchive")
file_name=camera_alembic.parm("fileName")
file_name.set(dict_all["layout"])
buildHierarchy=camera_alembic.parm("buildHierarchy")
buildHierarchy.pressButton()
hou.cd("/obj/alembicarchive1/camera1/")
cameraShape=hou.node("cameraShape1")
reslution= cameraShape.parmTuple("res")
reslution.set((int(dict_all["camera_resultion_wight"]),int(dict_all["camera_resultion_hight"])))
#创建资产alembic节点
if dict_all["assets"]!=[]:
    # 创建材质节点
    hou.cd("/mat")
    matPwd = hou.node("/mat")
    bricksNode = matPwd.createNode("bricks")
    principledshaderNode = matPwd.createNode("principledshader::2.0")
    hou.cd("/obj")
    assetNode=hou.node("/obj")
    geometry = assetNode.createNode("geo")
    geometry.setName("assetGeometry")
    hou.cd("/obj/assetGeometry")
    assetPwd = hou.pwd()
    for assets in range(len(dict_all["assets"])):
        assets_alembic=assetPwd.createNode("alembic")
        file_name_assets=assets_alembic.parm("fileName")
        file_name_assets.set(dict_all["assets"][assets])
        if dict_all["assets"]==[]:
            assets_alembic.bypass(1)
        else:
            uvLayout = assetPwd.createNode("uvlayout")
            matNode = assetPwd.createNode("material")
            uvLayout.setFirstInput(assets_alembic)
            matNode.setFirstInput(uvLayout)
    assetMerge = assetPwd.createNode("merge")

    materialsNode =toolutils.findAllChildNodesOfType(hou.pwd(), 'material', True)
    # materials = toolutils.findAllChildNodesOfType(matPwd, 'material', True)
    materials = [bricksNode,principledshaderNode]
    for each in xrange(len(materialsNode)):
        materialsNode[each].parm("shop_materialpath1").set("/mat/%s"%materials[each])
        assetMerge.setNextInput(materialsNode[each])

    assetMerge.setDisplayFlag(True)
    assetMerge.setRenderFlag(True)
else:
    pass

#创建animation_alembic节点
if dict_all["animation"]!=[]:
    hou.cd("/obj")
    objPwd = hou.pwd()
    animationGeo = objPwd.createNode("geo")
    animationGeo.setName("animationGeometry")
    hou.cd("/obj/animationGeometry")
    animationAlembicPwd = hou.pwd()
    animationAlembicNode = animationAlembicPwd.createNode("alembic")
    fileAnimationNamePath = animationAlembicNode.parm("fileName")
    fileAnimationNamePath.set(dict_all["animation"])
    animationAlembicNode.setRenderFlag(True)
else:
    pass

#创建FX_alembic节点
if dict_all["FX"]!=[]:
    hou.cd("/obj")
    objPwd = hou.pwd()
    animationGeo = objPwd.createNode("geo")
    animationGeo.setName("fxGeometry")
    hou.cd("/obj/fxGeometry")
    fxAlembicPwd = hou.pwd()
    fxAlembicNode = fxAlembicPwd.createNode("alembic")
    fileFxNamePath = fxAlembicNode.parm("fileName")
    fileFxNamePath.set(dict_all["FX"])
    fxAlembicNode.setRenderFlag(True)
else:
    pass

#创建灯光
hou.cd("/")
obj_light=hou.node("/obj")
hight_light=obj_light.createNode("hlight")
hlight_exposure=hight_light.parm("light_exposure")
hlight_exposure.set(7.5)
hlight_intensity = hight_light.parm("light_intensity").set(10)

trans=hight_light.parmTuple("t")
trans.set((-25.2872,34.3461,-20.543))
rotate=hight_light.parmTuple("r")
rotate.set((90,0,0))


hou.cd("/obj")
pwd=hou.pwd()
pwd.layoutChildren()
geo=hou.node("fxGeometry")
v_blur=geo.parm("geo_velocityblur")
v_blur.setPending(1)
#创建渲染器
out=hou.node("/out")
mantra=out.createNode("ifd")
trange=mantra.parm("trange")
trange.setPending(1)
frame=mantra.parmTuple("f")
frame.deleteAllKeyframes()
frame.set((int(dict_all["start_frame"]),int(dict_all["end_frame"]),1))
camera_name=mantra.parm("camera")
camera_name.set("/obj/alembicarchive1/camera1/cameraShape1")
render_engine=mantra.parm("vm_renderengine")
render_engine.set(dict_all["renderengine"])
blur=mantra.parm("allowmotionblur")
blur.setPending(1)

picture=mantra.parm("vm_picture")
picture.set(dict_all["save_pos"])
mantra.render()



