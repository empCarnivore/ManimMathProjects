from MF_Tools import *
from MF_Tools.dual_compatibility import *
from typing_extensions import override


class TransformByIndexMap(TransformByGlyphMap):
    def __init__(self,
        mobA,
        mobB,
        *glyph_map,
        from_copy=False,
        mobA_submobject_index=[],
        mobB_submobject_index=[],
        default_introducer=FadeIn,
        default_remover=FadeOut,
        introduce_individually=False,
        remove_individually=False,
        shift_fades=False,
        auto_fade=False,
        auto_resolve_delay=0,
        show_indices=False,
        A_index_labels_color=RED_D,
        B_index_labels_color=BLUE_D,
        index_label_height=0.2,
        printing=False,
        **kwargs):

        super().__init__(
            mobA,
            mobB,
            *glyph_map,
            from_copy=from_copy,
            mobA_submobject_index=mobA_submobject_index,
            mobB_submobject_index=mobB_submobject_index,
            default_introducer=default_introducer,
            default_remover=default_remover,
            introduce_individually=introduce_individually,
            remove_individually=remove_individually,
            shift_fades=shift_fades,
            auto_fade=auto_fade,
            auto_resolve_delay=auto_resolve_delay,
            show_indices=show_indices,
            A_index_labels_color=A_index_labels_color,
            B_index_labels_color=B_index_labels_color,
            index_label_height=index_label_height,
            printing=printing,
            **kwargs)