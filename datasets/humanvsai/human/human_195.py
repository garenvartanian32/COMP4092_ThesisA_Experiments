def display_trajectory(sys, times, coords_list, box_vectors=None,
                       style='spheres'):
    v = QtTrajectoryViewer()
    
    v.add_post_processing(SSAOEffect)
    v.add_post_processing(FXAAEffect)
    v.add_post_processing(GammaCorrectionEffect, 1.60)
    
    if style == 'spheres':
        backend = 'impostors'
    elif style == 'points':
        backend = 'points'
    else:
        raise Exception("No such style")
        
    sr = v.add_renderer(AtomRenderer, sys.r_array, sys.type_array,
                        backend=backend)
    
    if sys.box_vectors is not None:
        br = v.add_renderer(BoxRenderer, sys.box_vectors)
        # We autozoom on the box
        a, b, c = sys.box_vectors
        box_vertices = np.array([[0.0, 0.0, 0.0],
                                 a, b, c,
                                 a + b, a + c, b + c,
                                 a + b + c])
        v.widget.camera.autozoom(box_vertices)
    else:
        v.widget.camera.autozoom(sys.r_array)
    
    v.set_ticks(len(coords_list))
    @v.update_function
    def on_update(index):
        sr.update_positions(coords_list[index])
        if box_vectors is not None:
            br.update(box_vectors[index])
        v.set_text(format_time(times[index]))
        v.widget.repaint()
    v.run()