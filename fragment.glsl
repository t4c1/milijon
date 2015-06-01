//GLSL 
#version 140
#extension GL_ARB_compatibility : enable 

uniform sampler2D p3d_Texture0; 

void main() {
  gl_FragColor = texture2D(p3d_Texture0, gl_TexCoord[0].st);
}