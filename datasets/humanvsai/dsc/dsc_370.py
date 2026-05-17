import io

def _send_streamify(self, frame):
    """Helper method to streamify a frame."""
    # Convert the frame to bytes
    frame_bytes = io.BytesIO()
    frame.save(frame_bytes, format='JPEG')
    frame_bytes.seek(0)

    # Streamify the frame
    self.wfile.write(frame_bytes.getvalue())