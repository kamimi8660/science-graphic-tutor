from PIL import Image, ImageDraw, ImageFont
import argparse
import textwrap

def create_card(image_path, title, principles, steps, errors, test_points, output_path):
    try:
        base_img = Image.open(image_path)
        if base_img.mode != 'RGB':
            base_img = base_img.convert('RGB')
        img_w, img_h = base_img.size

        draw = ImageDraw.Draw(base_img)

        # Force right 45% to pure white so text is always legible
        text_bg_x = int(img_w * 0.55)
        draw.rectangle([(text_bg_x, 0), (img_w, img_h)], fill=(255, 255, 255))
        # Thin separator line
        draw.line([(text_bg_x, 0), (text_bg_x, img_h)], fill=(210, 210, 210), width=2)

        text_area_x = int(img_w * 0.57)
        text_area_w = int(img_w * 0.40)

        # Use Hiragino Sans GB for best Chinese rendering on macOS
        font_path_bold = "/System/Library/Fonts/Hiragino Sans GB.ttc"
        font_path_light = "/System/Library/Fonts/STHeiti Light.ttc"
        try:
            font_title = ImageFont.truetype(font_path_bold, 52)
            font_heading = ImageFont.truetype(font_path_bold, 36)
            font_body = ImageFont.truetype(font_path_light, 28)
        except Exception as e:
            print(f"Font loading error: {e}, falling back to STHeiti")
            try:
                font_title = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 52)
                font_heading = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 36)
                font_body = ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc", 28)
            except:
                font_title = ImageFont.load_default()
                font_heading = ImageFont.load_default()
                font_body = ImageFont.load_default()

        color_title = (50, 50, 55)
        color_heading_principle = (0, 102, 180)   # Blue
        color_heading_steps = (0, 140, 70)        # Green
        color_heading_errors = (200, 50, 50)       # Red
        color_heading_exam = (180, 100, 0)         # Orange
        color_body = (70, 70, 75)

        current_y = int(img_h * 0.06)

        # --- Title ---
        draw.text((text_area_x, current_y), title, font=font_title, fill=color_title)
        current_y += 75
        # Underline
        draw.line([(text_area_x, current_y), (text_area_x + text_area_w - 40, current_y)], fill=(200, 200, 200), width=2)
        current_y += 30

        def draw_section(heading, content, y_pos, heading_color):
            draw.text((text_area_x, y_pos), heading, font=font_heading, fill=heading_color)
            y_pos += 50

            chars_per_line = 18
            lines = textwrap.wrap(content, width=chars_per_line)
            for line in lines:
                draw.text((text_area_x, y_pos), line, font=font_body, fill=color_body)
                y_pos += 42
            return y_pos + 30

        current_y = draw_section("核心原理", principles, current_y, color_heading_principle)
        current_y = draw_section("关键要素", steps, current_y, color_heading_steps)
        current_y = draw_section("易错警示", errors, current_y, color_heading_errors)
        current_y = draw_section("考试高频", test_points, current_y, color_heading_exam)

        base_img.save(output_path)
        print(f"Successfully generated full card at {output_path}")
        return True

    except Exception as e:
        print(f"Error creating card: {e}")
        import traceback
        traceback.print_exc()
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
