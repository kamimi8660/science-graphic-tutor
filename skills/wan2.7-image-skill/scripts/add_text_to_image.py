from PIL import Image, ImageDraw, ImageFont
import argparse
import textwrap

def create_card(image_path, title, principles, steps, errors, test_points, output_path):
    try:
        base_img = Image.open(image_path)
        
        TARGET_W, TARGET_H = 1774, 1254
        left_w = int(TARGET_W * 0.55)
        
        ratio = max(left_w / base_img.width, TARGET_H / base_img.height)
        new_w, new_h = int(base_img.width * ratio), int(base_img.height * ratio)
        base_img = base_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        cx, cy = (new_w - left_w) // 2, (new_h - TARGET_H) // 2
        base_img = base_img.crop((cx, cy, cx + left_w, cy + TARGET_H))
        
        final_img = Image.new('RGB', (TARGET_W, TARGET_H), (255, 255, 255))
        final_img.paste(base_img, (0, 0))
        
        img_w, img_h = TARGET_W, TARGET_H
        text_area_x = int(img_w * 0.55)
        
        draw = ImageDraw.Draw(final_img)
        draw.line([(text_area_x, 0), (text_area_x, img_h)], fill=(210, 210, 210), width=2)
        
        import os
        def get_fallback_chinese_font():
            candidate_paths = [
                '/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
                '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
                '/usr/share/fonts/truetype/arphic/uming.ttc',
                '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
                '/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc',
                '/System/Library/Fonts/STHeiti Medium.ttc',
                '/System/Library/Fonts/PingFang.ttc',
                'C:/Windows/Fonts/msyh.ttc',
                'C:/Windows/Fonts/simhei.ttf'
            ]
            for path in candidate_paths:
                if os.path.exists(path):
                    return path
            
            try:
                import subprocess
                result = subprocess.run(['fc-list', ':lang=zh', 'file'], capture_output=True, text=True)
                for line in result.stdout.split('\n'):
                    if ':' in line:
                        potential_path = line.split(':')[0].strip()
                        if os.path.exists(potential_path) and potential_path.lower().endswith(('.ttf', '.ttc', '.otf')):
                            return potential_path
            except Exception:
                pass
            
            # Global fallback: find ANY font in /usr/share/fonts
            if os.path.exists('/usr/share/fonts'):
                for root, _, files in os.walk('/usr/share/fonts'):
                    for file in files:
                        if file.lower().endswith(('.ttc', '.ttf')):
                            return os.path.join(root, file)
                            
            return None

        font_path = get_fallback_chinese_font()
        
        try:
            if font_path:
                font_title = ImageFont.truetype(font_path, 34)
                font_heading = ImageFont.truetype(font_path, 26)
                font_body = ImageFont.truetype(font_path, 19)
            else:
                raise Exception("No fallback Chinese font could be found on this system.")
        except Exception as e:
            print(f"Font loading error: {e}")
            font_title = ImageFont.load_default()
            font_heading = ImageFont.load_default()
            font_body = ImageFont.load_default()

        color_primary = (40, 40, 44)    
        color_accent = (210, 60, 60)
        color_secondary = (70, 70, 75)
        
        current_y = 80
        
        draw.text((text_area_x + 30, current_y), title, font=font_title, fill=color_primary)
        current_y += 80

        def draw_section(heading, content, y_pos):
            draw.text((text_area_x + 30, y_pos), heading, font=font_heading, fill=color_accent)
            y_pos += 45
            
            lines = textwrap.wrap(content, width=28) 
            for line in lines:
                draw.text((text_area_x + 30, y_pos), line, font=font_body, fill=color_secondary)
                y_pos += 38
            return y_pos + 25
            
        current_y = draw_section("核心原理", principles, current_y)
        current_y = draw_section("关键要素", steps, current_y)
        current_y = draw_section("易错警示", errors, current_y)
        current_y = draw_section("考试高频", test_points, current_y)

        final_img.save(output_path)
        print(f"Successfully generated full card at {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating card: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--principles", required=True)
    parser.add_argument("--steps", required=True)
    parser.add_argument("--errors", required=True)
    parser.add_argument("--points", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    create_card(args.image, args.title, args.principles, args.steps, args.errors, args.points, args.output)
