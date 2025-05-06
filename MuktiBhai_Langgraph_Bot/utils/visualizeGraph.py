import os

def draw_graph(graph):
    try:
        output_dir = "graph_visualization"
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, "graph.png")

        # Ensure graph object retrieval does not fail
        graph_obj = graph.get_graph()
        if not graph_obj:
            raise ValueError("Failed to retrieve graph object.")

        # Generate the image in bytes
        image_data = graph_obj.draw_mermaid_png()
        if not image_data:
            raise ValueError("Failed to generate graph image.")

        # Save the image manually
        with open(output_file, "wb") as f:
            f.write(image_data)

        print(f"Graph Image saved to {output_file}")

    except Exception as e:
        print(e)
