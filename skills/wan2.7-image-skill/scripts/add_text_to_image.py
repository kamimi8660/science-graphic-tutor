from PIL import Image, ImageDraw, ImageFont
import argparse
import textwrap

def create_card(image_path, title, principles, steps, errors, test_points, output_path):
    try:
        base_img = Image.open(image_path)
        img_w, img_h = base_img.size
        
        text_area_x = int(img_w * 0.55)
        text_area_w = int(img_w * 0.40)
        
        draw = ImageDraw.Draw(base_img)
        
        # Force right 45% to pure white background
        draw.rectangle([(text_area_x, 0), (img_w, img_h)], fill=(255, 255, 255))
        draw.line([(text_area_x, 0), (text_area_x, img_h)], fill=(210, 210, 210), width=2)
        
        import os
        def get_fallback_chinese_font():
            candidate_paths = [
                '/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
                '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
                '/usr/share/fonts/truetype/arphic/uming.ttc',
                '/System/Library/Fonts/STHeiti Medium.ttc',
                '/System/Library/Fonts/PingFang.ttc'
            ]
            for path in candidate_paths:
                if os.path.exists(path):
                    return path
            
            try:
                import subprocess
                result = subprocess.run(['fc-list', ':lang=zh', 'file'], capture_output=True, text=True)
                if result.stdout:
                    first_font = result.stdout.split('\n')[0].split(':')[0].strip()
                    if os.path.exists(first_font):
                        return first_font
            except Exception:
                pass
            return None

        font_path = get_fallback_chinese_font()
        
        try:
            if font_path:
                font_title = ImageFont.truetype(font_path, 42)
                font_heading = ImageFont.truetype(font_path, 32)
                font_body = ImageFont.truetype(font_path, 24)
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
        
        draw.text((text_area_x, current_y), title, font=font_title, fill=color_primary)
        current_y += 80

        def draw_section(heading, content, y_pos):
            draw.text((text_area_x, y_pos), heading, font=font_heading, fill=color_accent)
            y_pos += 45
            
            lines = textwrap.wrap(content, width=22) 
            for line in lines:
                draw.text((text_area_x, y_pos), line, font=font_body, fill=color_secondary)
                y_pos += 38
            return y_pos + 25
            
        current_y = draw_section("核心原理", principles, current_y)
        current_y = draw_section("关键要素", steps, current_y)
        current_y = draw_section("易错警示", errors, current_y)
        current_y = draw_section("考试高频", test_points, current_y)

        base_img.save(output_path)
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
