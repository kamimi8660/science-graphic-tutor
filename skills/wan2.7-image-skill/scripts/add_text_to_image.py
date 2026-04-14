import argparse
from PIL import Image, ImageDraw, ImageFont
import textwrap

def draw_text(image_path, title, principles, steps, errors, points, output_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    # FORCE white background on the right 50% in case the model failed to leave it pure white
    split_x = int(width * 0.50)
    draw.rectangle([(split_x, 0), (width, height)], fill=(255, 255, 255))
    # Draw vertical separator
    draw.line([(split_x, 0), (split_x, height)], fill=(200, 200, 200), width=2)
    
    start_x = int(width * 0.54)
    margin_y = int(height * 0.1)
    max_width = int(width * 0.42)
    
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 60)
        font_header = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
        font_body = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 30)
    except IOError:
        font_title = ImageFont.load_default()
        font_header = ImageFont.load_default()
        font_body = ImageFont.load_default()

    current_y = margin_y
    
    def write_block(header, text, y_pos, header_color=(200, 50, 50), body_color=(80, 80, 80)):
        if header:
            draw.text((start_x, y_pos), header, font=font_header, fill=header_color)
            y_pos += 60
        if text:
            # English/Chinese text wrap approximation
            chars_per_line = max_width // 30
            lines = textwrap.wrap(text, width=chars_per_line)
            for line in lines:
                draw.text((start_x, y_pos), line, font=font_body, fill=body_color)
                y_pos += 45
        return y_pos + 40

    # Title
    draw.text((start_x, current_y), f"{title}", font=font_title, fill=(50, 50, 50))
    current_y += 100
    
    current_y = write_block("核心原理", principles, current_y)
    current_y = write_block("关键要素", steps, current_y)
    current_y = write_block("易错警示", errors, current_y)
    if points and points.strip():
        current_y = write_block("考试高频", points, current_y)
        
    img.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--principles", required=True)
    parser.add_argument("--steps", required=True)
    parser.add_argument("--errors", required=True)
    parser.add_argument("--points", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    draw_text(args.image, args.title, args.principles, args.steps, args.errors, args.points, args.output)
