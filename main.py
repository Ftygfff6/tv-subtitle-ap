from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import arabic_reshaper
from bidi.algorithm import get_display

class GameSubtitleOverlay(FloatLayout):
    def __init__(self, **kwargs):
        super(GameSubtitleOverlay, self).__init__(**kwargs)
        
        # النص التجريبي للترجمة (يمكنك تحديثه لاحقاً حسب مصدر الترجمة)
        raw_text = "أهلاً بك يا فيصل، جاري اختبار ترجمة الألعاب على الشاشة..."
        
        # معالجة النص العربي لضمان ترتيب الحروف واتجاهها بشكل صحيح
        reshaped_text = arabic_reshaper.reshape(raw_text)
        bidi_text = get_display(reshaped_text)
        
        # إنشاء حاوية نص الترجمة بستايل الألعاب
        self.sub_label = Label(
            text=bidi_text,
            font_size=36,               # حجم خط كبير وواضح ومناسب للشاشات الكبيرة
            color=(1, 1, 1, 1),         # لون النص أبيض ناصح
            halign='center',
            valign='middle',
            size_hint=(0.85, 0.12),     # عرض الشريط وطوله
            pos_hint={'center_x': 0.5, 'y': 0.06}, # مكان الشريط أسفل الشاشة تماماً
            text_size=(self.width * 0.85, None)
        )
        
        # تحديث أبعاد النص تلقائياً عند تغيير المقاسات
        self.sub_label.bind(size=self.update_text_size)
        
        # إضافة خلفية شريطية داكنة شبه شفافة خلف النص (مثل ستايل الألعاب)
        with self.sub_label.canvas.before:
            # لون أسود شفاف (RGBA: أسود بنسبة شفافية 60% ليعطي مظهر سينمائي)
            self.bg_color = Color(0, 0, 0, 0.6) 
            self.bg_rect = Rectangle(size=self.sub_label.size, pos=self.sub_label.pos)
            
        # ربط تحديث مكان وحجم الخلفية مع حركة النص
        self.sub_label.bind(pos=self.update_bg, size=self.update_bg)
        
        # إضافة العنصر للنافذة العائمة
        self.add_widget(self.sub_label)

    def update_text_size(self, instance, value):
        instance.text_size = (value[0], None)

    def update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

class SubtitleApp(App):
    def build(self):
        return GameSubtitleOverlay()

if __name__ == '__main__':
    SubtitleApp().run()
