/* Header for module uptext, generated by p2c 1.21alpha-07.Dec.93 */
#ifndef UPTEXT_H
#define UPTEXT_H


#ifdef UPTEXT_G
# define vextern
#else
# define vextern extern
#endif
/* Insert and translate uptext */


extern void initUptext(void);
extern void clearUptext(void);
extern short uptextLineNo(short voice);
extern void setUptextLineNo(short voice, short lno);
extern void addUptext(short voice, boolean *no_uptext, Char *pretex);


#undef vextern

#endif /*UPTEXT_H*/

/* End. */
