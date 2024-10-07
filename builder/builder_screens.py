import flet as ft

class screen_view(ft.Container):

    def __init__(self,
                    page,
                    bgcolor: str="Transparent",
                    width: int=0,
                    height: int=0,
                    padding: tuple=(0,0,0,0),
                    content=ft.Container(),
                    alignment=ft.alignment.center,
                    pos_hint: tuple=(0,0),
                    visible: bool=True,
        ):
        super().__init__()
         # MAIN PAGE
        self.var_scope = 'text var'
        self.page=page
        self.content_widget = content
        self.tmp_padding = padding
        self.tmp_offset = pos_hint
        self.visible = visible

        self.height =  self.page.height
        self.height = self.page.height
        # self.expand          = True
        self.ink             = False
        self.bgcolor         = bgcolor
        # self.padding = ft.padding.only(left=0,top=0,right=0,bottom=60)
        # self.margin = ft.margin.all(24)
        # self.padding         = ft.padding.only(
        #                         left=self.tmp_padding[0],
        #                         top=self.tmp_padding[1],
        #                         right=self.tmp_padding[2],
        #                         bottom=self.tmp_padding[3])  if self.tmp_padding == tuple() else ft.padding.all(self.tmp_padding)

        # OPCITY
        self.animate_opacity = 200

        # ROTATE
        self.rotate = ft.transform.Rotate(0, alignment=ft.alignment.center)
        self.animate_rotation = ft.animation.Animation(
            300, )

        # SCALE
        self.scale = ft.transform.Scale(scale=1)
        self.animate_scale = ft.animation.Animation(
            150, )

        # ANIMATE
        self.offset = ft.transform.Offset(0, 0)
        self.animate_offset = ft.animation.Animation(100,)

        # BOUNCE
        self.animate = ft.animation.Animation(
            1000, ft.AnimationCurve.BOUNCE_OUT)
        # ======================= ANIMATION
        # self.shadow = ft.BoxShadow(
        #     spread_radius=1,
        #     blur_radius=15,
        #     color=ft.colors.BLACK,
        #     offset=ft.Offset(0, 0),
        #     blur_style=ft.ShadowBlurStyle.OUTER,
        # )

    def build(self):
        self.content=self.content_widget