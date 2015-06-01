//GLSL
#version 140
#extension GL_ARB_compatibility : enable

uniform mat4 p3d_ModelViewProjectionMatrix;
in vec4 p3d_Vertex;
in vec4 p3d_MultiTexCoord0;
uniform vec4 shader_data[200];

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * (p3d_Vertex + shader_data[ gl_InstanceID ] );
  //gl_Position = p3d_ModelViewProjectionMatrix * (p3d_Vertex + vec4(gl_InstanceID,gl_InstanceID,gl_InstanceID,0) );
  gl_TexCoord[0] = p3d_MultiTexCoord0;
}
