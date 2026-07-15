---
title: "Modifiers"
description: "Jetpack Compose layout modifiers for @expo/ui components."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/modifiers.md"
scraped_at: "2026-07-15T09:00:26.740478"
---

---
title: Modifiers
description: Jetpack Compose layout modifiers for @expo/ui components.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Modifiers

Jetpack Compose layout modifiers for @expo/ui components.
Android, Included in Expo Go

Jetpack Compose modifiers allow you to customize the layout, appearance, and behavior of UI components. Modifiers are the Compose equivalent of style properties — they control sizing, padding, backgrounds, interactions, and more.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

Modifiers are applied to components using the `modifiers` prop with an array syntax. You can combine multiple modifiers to create complex styling and behavior. Modifiers are applied in the order they appear in the array, which can affect the final result (for example, applying `padding` before `background` produces different results than the reverse).

```tsx
import { Button, Host } from '@expo/ui/jetpack-compose';
import {
  paddingAll,
  fillMaxWidth,
  background,
  border,
  shadow,
  clickable,
} from '@expo/ui/jetpack-compose/modifiers';

function ModifiersExample() {
  return (
    <Host style={{ flex: 1 }}>
      {/* Basic styling modifiers */}
      <Button modifiers={[paddingAll(16), fillMaxWidth(), background('#FF6B6B')]}>
        Full-width padded button
      </Button>

      {/* Complex combination with border and shadow */}
      <Button modifiers={[paddingAll(12), background('#4ECDC4'), border(2, '#2C3E50'), shadow(4)]}>
        Styled with border and shadow
      </Button>
    </Host>
  );
}
```

## Padding

Control the spacing around a component's content.

### `paddingAll(all)`

Applies equal padding on all four sides.

| Parameter | Type | Description |
| --- | --- | --- |
| `all` | `number` | Padding value in dp. |

```tsx
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[paddingAll(16)]}>Padded button</Button>;
```

### `padding(start, top, end, bottom)`

Applies individual padding to each side.

| Parameter | Type | Description |
| --- | --- | --- |
| `start` | `number` | Left/start padding in dp. |
| `top` | `number` | Top padding in dp. |
| `end` | `number` | Right/end padding in dp. |
| `bottom` | `number` | Bottom padding in dp. |

```tsx
import { padding } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[padding(16, 8, 16, 8)]}>Custom padding</Button>;
```

## Size

Control the dimensions of a component.

### `size(width, height)`

Sets exact dimensions for the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `width` | `number` | Width in dp. |
| `height` | `number` | Height in dp. |

```tsx
import { size } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[size(200, 48)]}>Fixed size</Button>;
```

### `fillMaxSize(fraction?)`

Fills all available space in both dimensions.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction` | `number` | Fraction of available space (0.0–1.0). Default `1.0`. |

```tsx
import { fillMaxSize } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[fillMaxSize()]}>Fill all space</Button>
<Button modifiers={[fillMaxSize(0.5)]}>Fill half</Button>
```

### `fillMaxWidth(fraction?)`

Fills available width.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction` | `number` | Fraction of available width (0.0–1.0). Default `1.0`. |

```tsx
import { fillMaxWidth } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[fillMaxWidth()]}>Full width</Button>;
```

### `fillMaxHeight(fraction?)`

Fills available height.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction` | `number` | Fraction of available height (0.0–1.0). Default `1.0`. |

### `width(value)`

Sets an exact width.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | Width in dp. |

### `height(value)`

Sets an exact height.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | Height in dp. |

### `wrapContentWidth(alignment?)`

Sizes the component to wrap its content width.

| Parameter | Type | Description |
| --- | --- | --- |
| `alignment` | `string` | Horizontal alignment of the content. |

### `wrapContentHeight(alignment?)`

Sizes the component to wrap its content height.

| Parameter | Type | Description |
| --- | --- | --- |
| `alignment` | `string` | Vertical alignment of the content. |

## Position

Control the position of a component relative to its natural placement.

### `offset(x, y)`

Offsets the component from its natural position without affecting the layout of surrounding components.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `number` | Horizontal offset in dp. |
| `y` | `number` | Vertical offset in dp. |

```tsx
import { offset } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[offset(10, 5)]}>Offset button</Button>;
```

## Appearance

Control the visual appearance of a component.

### `background(color)`

Sets the background color.

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | `string` | Background color (hex string). |

```tsx
import { background } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[background('#3498DB')]}>Blue background</Button>;
```

### `border(borderWidth, borderColor)`

Adds a border around the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `borderWidth` | `number` | Border width in dp. |
| `borderColor` | `string` | Border color (hex string). |

```tsx
import { border } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[border(2, '#E74C3C')]}>Bordered button</Button>;
```

### `shadow(elevation)`

Adds an elevation shadow beneath the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `elevation` | `number` | Shadow elevation in dp. |

```tsx
import { shadow } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[shadow(8)]}>Elevated button</Button>;
```

### `dropShadow(shape, config?)`

Draws a shadow behind the component with control over the blur radius, spread, offset, and color. Unlike `shadow`, it does not require an elevation value.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | `Shape` | The shape of the shadow (see the shapes table below). |
| `config.radius` | `number` | Blur radius in dp. |
| `config.spread` | `number` | Amount to expand (positive) or contract (negative) in dp. |
| `config.color` | `string` | Shadow color (hex string). Defaults to black. |
| `config.offsetX` | `number` | Horizontal offset in dp. |
| `config.offsetY` | `number` | Vertical offset in dp. |
| `config.alpha` | `number` | Shadow opacity (0.0–1.0). |

```tsx
import { dropShadow, Shapes } from '@expo/ui/jetpack-compose/modifiers';

<Button
  modifiers={[
    dropShadow(Shapes.RoundedCorner(24), { radius: 16, spread: 4, color: '#6200EE', offsetY: 8 }),
  ]}>
  Drop shadow
</Button>;
```

### `innerShadow(shape, config?)`

Draws a shadow inside the component to create an inset effect. Apply the `background` modifier before `innerShadow` so the shadow renders.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | `Shape` | The shape of the shadow (see the shapes table below). |
| `config.radius` | `number` | Blur radius in dp. |
| `config.spread` | `number` | Amount to expand (positive) or contract (negative) in dp. |
| `config.color` | `string` | Shadow color (hex string). Defaults to black. |
| `config.offsetX` | `number` | Horizontal offset in dp. |
| `config.offsetY` | `number` | Vertical offset in dp. |
| `config.alpha` | `number` | Shadow opacity (0.0–1.0). |

```tsx
import { innerShadow, background, Shapes } from '@expo/ui/jetpack-compose/modifiers';

<Button
  modifiers={[
    background('#FFFFFF'),
    innerShadow(Shapes.RoundedCorner(24), { radius: 16, spread: 2, offsetY: 6 }),
  ]}>
  Inner shadow
</Button>;
```

### `alpha(alpha)`

Controls the opacity of the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `alpha` | `number` | Opacity value (0.0–1.0). |

```tsx
import { alpha } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[alpha(0.5)]}>Semi-transparent</Button>;
```

### `blur(radius)`

Applies a blur effect to the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `radius` | `number` | Blur radius in dp. |

```tsx
import { blur } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[blur(4)]}>Blurred button</Button>;
```

## Shadow recipes

Common shadow styles are combinations of the `dropShadow` and `innerShadow` modifiers rather than separate APIs. Because the `modifiers` prop takes an array, you stack and tune the shadow modifiers to build each style.

### Neobrutalist shadow

A neobrutalist shadow is a hard-edged drop shadow with no blur and a thick border. Set `radius` and `spread` to `0`, then offset the shadow.

```tsx
import { dropShadow, border, background, Shapes } from '@expo/ui/jetpack-compose/modifiers';

<Box
  modifiers={[
    dropShadow(Shapes.Rectangle, {
      radius: 0,
      spread: 0,
      offsetX: 8,
      offsetY: 8,
      color: '#000000',
    }),
    border(8, '#000000'),
    background('#FFFFFF'),
  ]}
/>;
```

### Neumorphic shadow

A neumorphic shadow layers two drop shadows on a surface that shares its background color: a light shadow toward the light source and a darker shadow on the opposite side. Apply both before the `background`.

```tsx
import { dropShadow, background, Shapes } from '@expo/ui/jetpack-compose/modifiers';

const shape = Shapes.RoundedCorner(24);

<Box
  modifiers={[
    dropShadow(shape, { radius: 15, offsetX: -10, offsetY: -10, color: '#FFFFFF' }),
    dropShadow(shape, { radius: 15, offsetX: 10, offsetY: 10, color: '#B1B1B1' }),
    background('#E0E0E0'),
  ]}
/>;
```

To create the pressed, recessed variant, use two `innerShadow` modifiers instead and place them after the `background`.

## Transform

Apply visual transformations to a component.

### `rotate(degrees)`

Rotates the component.

| Parameter | Type | Description |
| --- | --- | --- |
| `degrees` | `number` | Rotation angle in degrees. |

```tsx
import { rotate } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[rotate(45)]}>Rotated</Button>;
```

### `zIndex(index)`

Controls the drawing order of overlapping components.

| Parameter | Type | Description |
| --- | --- | --- |
| `index` | `number` | Layer index. |

```tsx
import { zIndex } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[zIndex(10)]}>On top</Button>;
```

## Animation

Animate layout changes within a component.

### `animateContentSize(dampingRatio?, stiffness?)`

Animates size changes of the component's content using a spring animation.

| Parameter | Type | Description |
| --- | --- | --- |
| `dampingRatio` | `number` | Spring damping ratio. Controls bounciness. |
| `stiffness` | `number` | Spring stiffness. Controls animation speed. |

```tsx
import { animateContentSize } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[animateContentSize()]}>Animated size</Button>
<Button modifiers={[animateContentSize(0.5, 200)]}>Custom spring</Button>
```

## Layout

Control how a component is sized and positioned within its parent container.

### `weight(weight)`

Assigns a flexible weight to a component inside a `Row` or `Column`, distributing available space proportionally among weighted children.

| Parameter | Type | Description |
| --- | --- | --- |
| `weight` | `number` | Weight factor. |

```tsx
import { weight } from '@expo/ui/jetpack-compose/modifiers';

// In a Row, the first button takes 2/3 and the second takes 1/3
<Button modifiers={[weight(2)]}>Wider</Button>
<Button modifiers={[weight(1)]}>Narrower</Button>
```

### `align(alignment)`

Sets the alignment of the component within its parent container.

| Parameter | Type | Description |
| --- | --- | --- |
| `alignment` | `string` | Alignment within the container. |

### `matchParentSize()`

Sizes the component to match the size of its parent `Box`. Unlike `fillMaxSize`, this does not affect the parent's measurement.

```tsx
import { matchParentSize } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[matchParentSize()]}>Match parent</Button>;
```

## Interaction

Add user interaction handlers to a component.

### `clickable(handler)`

Makes the component respond to click events.

| Parameter | Type | Description |
| --- | --- | --- |
| `handler` | `() => void` | Callback invoked on click. |

```tsx
import { clickable } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[clickable(() => console.log('Clicked!'))]}>Clickable</Button>;
```

### `combinedClickable(handlers, options?)`

Makes the component respond to both short-tap and long-press gestures. Wraps Compose's `Modifier.combinedClickable`. Useful for opening a [`DropdownMenu`](/versions/latest/sdk/ui/jetpack-compose/dropdownmenu.md) on long-press while keeping a separate short-tap action on the same view.

| Parameter | Type | Description |
| --- | --- | --- |
| `handlers.onClick` | `() => void` | Optional callback invoked on a short tap. |
| `handlers.onLongClick` | `() => void` | Optional callback invoked on a long press. |
| `options.indication` | `boolean` | Whether to show a ripple indication. Defaults to `true`. |

```tsx
import { combinedClickable } from '@expo/ui/jetpack-compose/modifiers';

<Text
  modifiers={[
    combinedClickable({
      onClick: () => console.log('Tapped'),
      onLongClick: () => setMenuExpanded(true),
    }),
  ]}>
  Long-press me
</Text>;
```

### `selectable(selected, handler)`

Makes the component selectable, similar to a radio button.

| Parameter | Type | Description |
| --- | --- | --- |
| `selected` | `boolean` | Whether the component is currently selected. |
| `handler` | `() => void` | Callback invoked when selection state changes. |

```tsx
import { selectable } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[selectable(isSelected, () => setIsSelected(!isSelected))]}>
  Selectable option
</Button>;
```

## Clipping

Clip a component's content to a specific shape.

### `clip(shape)`

Clips the component to the given shape. Content outside the shape boundary is not drawn.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | `Shape` | The shape to clip to. |

#### Available shapes

| Shape | Description |
| --- | --- |
| `Shapes.Rectangle` | A rectangle with no rounded corners. |
| `Shapes.Circle` | A perfect circle. |
| `Shapes.RoundedCorner(radius)` | A rectangle with uniform rounded corners. Pass a `number` for equal radius or an object `{ topStart, topEnd, bottomStart, bottomEnd }` for individual corner radii. |
| `Shapes.CutCorner(radius)` | A rectangle with cut (chamfered) corners. Accepts the same radius options as `RoundedCorner`. |
| `Shapes.Material.Cookie4Sided` | Material Design cookie shape with 4 sides. |
| `Shapes.Material.Cookie6Sided` | Material Design cookie shape with 6 sides. |

```tsx
import { clip } from '@expo/ui/jetpack-compose/modifiers';
import { Shapes } from '@expo/ui/jetpack-compose/modifiers';

// Circular clipping
<Button modifiers={[clip(Shapes.Circle)]}>Circle</Button>

// Rounded corners with uniform radius
<Button modifiers={[clip(Shapes.RoundedCorner(12))]}>Rounded</Button>

// Rounded corners with individual radii
<Button
  modifiers={[
    clip(Shapes.RoundedCorner({ topStart: 16, topEnd: 16, bottomStart: 0, bottomEnd: 0 })),
  ]}>
  Top rounded only
</Button>

// Cut corners
<Button modifiers={[clip(Shapes.CutCorner(8))]}>Cut corners</Button>
```

## Utility

### `testID(tag)`

Assigns a test identifier to the component for use in UI testing.

| Parameter | Type | Description |
| --- | --- | --- |
| `tag` | `string` | The test ID. |

```tsx
import { testID } from '@expo/ui/jetpack-compose/modifiers';

<Button modifiers={[testID('submit-button')]}>Submit</Button>;
```

## API

```tsx
import { paddingAll, padding, size, fillMaxWidth, background, clickable, clip, Shapes } from '@expo/ui/jetpack-compose/modifiers';
```

## Constants

### `Shapes`

Supported platforms: Android.

Type: { Circle: [BuiltinShape](#builtinshape), CutCorner: (params: number | [CornerRadii](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#cornerradii)) => [BuiltinShape](#builtinshape), Material: { Arch: [BuiltinShape](#builtinshape), Boom: [BuiltinShape](#builtinshape), Bun: [BuiltinShape](#builtinshape), Clover4Leaf: [BuiltinShape](#builtinshape), Clover8Leaf: [BuiltinShape](#builtinshape), Cookie12Sided: [BuiltinShape](#builtinshape), Cookie4Sided: [BuiltinShape](#builtinshape), Cookie6Sided: [BuiltinShape](#builtinshape), Cookie7Sided: [BuiltinShape](#builtinshape), Cookie9Sided: [BuiltinShape](#builtinshape), Diamond: [BuiltinShape](#builtinshape), Fan: [BuiltinShape](#builtinshape), Ghostish: [BuiltinShape](#builtinshape), Heart: [BuiltinShape](#builtinshape), Oval: [BuiltinShape](#builtinshape), Pentagon: [BuiltinShape](#builtinshape), Pill: [BuiltinShape](#builtinshape), PixelCircle: [BuiltinShape](#builtinshape), PixelTriangle: [BuiltinShape](#builtinshape), Puffy: [BuiltinShape](#builtinshape), PuffyDiamond: [BuiltinShape](#builtinshape), Slanted: [BuiltinShape](#builtinshape), SoftBurst: [BuiltinShape](#builtinshape), Sunny: [BuiltinShape](#builtinshape), Triangle: [BuiltinShape](#builtinshape), VerySunny: [BuiltinShape](#builtinshape) }, Rectangle: [BuiltinShape](#builtinshape), RoundedCorner: (params: number | [CornerRadii](/versions/v57.0.0/sdk/ui/jetpack-compose/shape.md#cornerradii)) => [BuiltinShape](#builtinshape) }

Predefined shapes for use with the `clip` modifier.

Example

```tsx
clip(Shapes.Circle)
clip(Shapes.RoundedCorner(16))
clip(Shapes.RoundedCorner({ topStart: 8, bottomEnd: 16 }))
clip(Shapes.Material.Heart)
```

## Methods

### `align(alignment)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `alignment` | [Alignment](#alignment) |

  

Aligns the view within its container.

Returns: `ModifierConfig`

### `alpha(alpha)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `alpha` | `number` | Opacity value (0.0 to 1.0). |

  

Sets the opacity/alpha of the view.

Returns: `ModifierConfig`

### `animateContentSize(dampingRatio, stiffness)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `dampingRatio`(optional) | `number` | Spring damping ratio. Default is `DampingRatioNoBouncy`. |
| `stiffness`(optional) | `number` | Spring stiffness. Default is `StiffnessMedium`. |

  

Animates size changes with spring animation.

Returns: `ModifierConfig`

### `animated(targetValue, spec)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `targetValue` | `number` |
| `spec`(optional) | [AnimationSpec](#animationspec) |

  

Returns: `{ $animated: true, animationSpec: AnimationSpec, targetValue: number }`

### `background(color, options)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | [ColorValue](https://reactnative.dev/docs/colors) | A color string (hex, e.g., `'#FF0000'`). |
| `options`(optional) | { animationSpec: [AnimationSpec](#animationspec) } | - |

  

Sets the background color. Pass an `animationSpec` to smoothly animate between colors when the prop changes (backed by `animateColorAsState`).

Returns: `ModifierConfig`

### `blur(radius)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `radius` | `number` | Blur radius in dp. |

  

Applies a blur effect.

Returns: `ModifierConfig`

### `border(borderWidth, borderColor)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `borderWidth` | `number` | Border width in dp. |
| `borderColor` | [ColorValue](https://reactnative.dev/docs/colors) | Border color string (hex). |

  

Adds a border around the view.

Returns: `ModifierConfig`

### `clickable(handler, options)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `handler` | `() => void` | Function to call when clicked. |
| `options`(optional) | `{ indication: boolean }` | Optional configuration. |

  

Makes the view clickable.

Returns: `ModifierConfig`

### `clip(shape)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | [BuiltinShape](#builtinshape) | A shape from `Shapes`, e.g. `Shapes.Circle` or `Shapes.Material.Heart`. |

  

Clips the view to a built-in Jetpack Compose shape.

Returns: `ModifierConfig`

### `combinedClickable(handlers, options)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `handlers` | `{ onClick: () => void, onLongClick: () => void }` | - |
| `options`(optional) | `{ indication: boolean }` | Optional configuration. |

  

Makes the view respond to both click and long-click gestures. Wraps Compose's `Modifier.combinedClickable`. Useful for triggering a `DropdownMenu` on long-press while keeping a separate short-press action.

Returns: `ModifierConfig`

### `createModifier(type, params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `params`(optional) | `Record<string, any>` |

  

Factory function to create modifier configuration objects.

Returns: `ModifierConfig`

### `defaultMinSize(options)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `options` | `{ minHeight: number, minWidth: number }` |

  

Constrain the size of the wrapped layout only when it would be otherwise unconstrained: the `minWidth` and `minHeight` constraints are only applied when the incoming corresponding constraint is `0`.

Returns: `ModifierConfig`

> **See:** [Compose `defaultMinSize` modifier](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#%28androidx.compose.ui.Modifier%29.defaultMinSize%28androidx.compose.ui.unit.Dp%2Candroidx.compose.ui.unit.Dp%29)

### `dropShadow(shape, config)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | [BuiltinShape](#builtinshape) | The shape of the shadow, for example `Shapes.RoundedCorner(16)` or `Shapes.Circle`. |
| `config`(optional) | [ShadowConfig](#shadowconfig) | Options that control the shadow's appearance. Default: `{}` |

  

Draws a shadow behind the view with control over the blur radius, spread, offset, and color. Unlike `shadow`, it does not require an elevation value.

Returns: `ModifierConfig`

### `fillMaxHeight(fraction)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction`(optional) | `number` | Fraction of max height (0.0 to 1.0). Default is 1.0. |

  

Fills the maximum available height.

Returns: `ModifierConfig`

### `fillMaxSize(fraction)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction`(optional) | `number` | Fraction of max size (0.0 to 1.0). Default is 1.0. |

  

Fills the maximum available size.

Returns: `ModifierConfig`

### `fillMaxWidth(fraction)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `fraction`(optional) | `number` | Fraction of max width (0.0 to 1.0). Default is 1.0. |

  

Fills the maximum available width.

Returns: `ModifierConfig`

### `graphicsLayer(params)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `params` | { alpha: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, ambientShadowColor: [ColorValue](https://reactnative.dev/docs/colors), cameraDistance: number, clip: boolean, compositingStrategy: 'auto' | 'offscreen' | 'modulate', rotationX: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, rotationY: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, rotationZ: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, scaleX: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, scaleY: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, shadowElevation: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, shape: [BuiltinShape](#builtinshape), spotShadowColor: [ColorValue](https://reactnative.dev/docs/colors), transformOriginX: number, transformOriginY: number, translationX: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number }, translationY: number | { $animated: true, animationSpec: [AnimationSpec](#animationspec), targetValue: number } } | Transform and visual effect parameters. |

  

Applies a graphics layer transformation with animation support.

Returns: `ModifierConfig`

> **See:** [Compose graphicsLayer documentation](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers).

### `height(value)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | Height in dp. |

  

Sets the exact height of the view.

Returns: `ModifierConfig`

### `horizontalScroll()`

Supported platforms: Android.

Makes the view horizontally scrollable. Wraps `Modifier.horizontalScroll(rememberScrollState())`. Use on a Row to create a non-lazy scrollable container.

Returns: `ModifierConfig`

### `imePadding()`

Supported platforms: Android.

Adds padding to avoid the software keyboard (IME). When the keyboard is visible, padding is added to keep content above it.

Returns: `ModifierConfig`

### `innerShadow(shape, config)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `shape` | [BuiltinShape](#builtinshape) | The shape of the shadow, for example `Shapes.RoundedCorner(16)` or `Shapes.Circle`. |
| `config`(optional) | [ShadowConfig](#shadowconfig) | Options that control the shadow's appearance. Default: `{}` |

  

Draws a shadow inside the view to create an inset effect. The view's `background` must come before this modifier for the shadow to render.

Returns: `ModifierConfig`

### `keyframes(params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `params` | `{ delayMillis: number, durationMillis: number, keyframes: Record<number, number> }` |

  

Returns: `{ $type: 'keyframes', delayMillis: number, durationMillis: number, keyframes: Record<number,> }</number,>`

### `matchParentSize()`

Supported platforms: Android.

Makes the view match the parent Box size. Only works when used inside Box.

Returns: `ModifierConfig`

### `menuAnchor(type, enabled)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `type`(optional) | `'primaryNotEditable'` | Anchor type. Currently only `'primaryNotEditable'` is supported. |
| `enabled`(optional) | `boolean` | Whether the anchor is enabled. Defaults to `true`. |

  

Marks a composable as the anchor for an `ExposedDropdownMenuBox`. Only works when used inside `ExposedDropdownMenuBox`.

Returns: `ModifierConfig`

### `offset(x, y)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `number` | Horizontal offset in dp. |
| `y` | `number` | Vertical offset in dp. |

  

Offsets the view from its natural position.

Returns: `ModifierConfig`

### `onGloballyPositioned(handler)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `handler` | `(layout: { height: number, width: number, x: number, y: number }) => void` | Function called with the new layout. |

  

Calls the handler whenever the composable is positioned, with its position and size. `x` and `y` are relative to the window. All values are in dp.

Returns: `ModifierConfig`

### `onSizeChanged(handler)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `handler` | `(size: { height: number, width: number }) => void` | Function called with the new size. |

  

Calls the handler whenever the composable's measured size changes. Sizes are in dp.

Returns: `ModifierConfig`

### `onVisibilityChanged(handler, options)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `handler` | `(isVisible: boolean) => void` | Function called with `true` when visible, `false` when not. |
| `options`(optional) | `{ minDurationMs: number, minFractionVisible: number }` | Optional configuration. |

  

Calls the handler when the composable's visibility changes (for example, enters or leaves the viewport in a lazy list).

Returns: `ModifierConfig`

### `padding(start, top, end, bottom)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `start` | `number` | Left padding in dp (or right in RTL). |
| `top` | `number` | Top padding in dp. |
| `end` | `number` | Right padding in dp (or left in RTL). |
| `bottom` | `number` | Bottom padding in dp. |

  

Applies padding with individual values for each side.

Returns: `ModifierConfig`

### `paddingAll(all)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `all` | `number` | Padding value in dp. |

  

Applies equal padding on all sides.

Returns: `ModifierConfig`

### `rotate(degrees)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `degrees` | `number` | Rotation angle in degrees. |

  

Rotates the view.

Returns: `ModifierConfig`

### `selectable(selected, handler, role)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `selected` | `boolean` | Whether the item is currently selected. |
| `handler` | `() => void` | Function to call when the item is clicked. |
| `role`(optional) | `'switch' | 'checkbox' | 'tab' | 'radioButton'` | Optional semantic role for accessibility: 'radioButton', 'checkbox', 'switch', or 'tab'. |

  

Makes the view selectable, like a radio button row.

Returns: `ModifierConfig`

### `selectableGroup()`

Supported platforms: Android.

Marks a column/row as a selectable group for accessibility. Screen readers will treat the children as a group of selectable items.

Returns: `ModifierConfig`

### `semantics(params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `params` | `{ contentType: string }` |

  

Applies semantic properties. Wraps `Modifier.semantics { ... }`.

Returns: `ModifierConfig`

### `shadow(elevation)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `elevation` | `number` | Shadow elevation in dp. |

  

Adds a shadow/elevation effect.

Returns: `ModifierConfig`

### `size(width, height)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `width` | `number` | Width in dp. |
| `height` | `number` | Height in dp. |

  

Sets exact width and height.

Returns: `ModifierConfig`

### `snap(params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `params`(optional) | `{ delayMillis: number }` |

  

Returns: `{ $type: 'snap', delayMillis: number }`

### `spring(params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `params`(optional) | `{ dampingRatio: number, stiffness: number, visibilityThreshold: number }` |

  

Returns: `{ $type: 'spring', dampingRatio: number, stiffness: number, visibilityThreshold: number }`

### `testID(tag)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `tag` | `string` | Test ID string. |

  

Sets the test ID for testing frameworks.

Returns: `ModifierConfig`

### `toggleable(value, handler, options)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `boolean` | The current toggle state. |
| `handler` | `() => void` | Function to call when toggled. |
| `options`(optional) | `{ role: 'switch' | 'checkbox' | 'tab' | 'radioButton' }` | Optional configuration. |

  

Makes the view toggleable with accessibility semantics. Use this to make a row containing a checkbox or switch tappable as a whole.

Returns: `ModifierConfig`

### `tween(params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `params`(optional) | `{ delayMillis: number, durationMillis: number, easing: 'linear' | 'ease' | 'fastOutSlowIn' | 'fastOutLinearIn' | 'linearOutSlowIn' }` |

  

Returns: `{ $type: 'tween', delayMillis: number, durationMillis: number, easing: 'linear' | 'ease' | 'fastOutSlowIn' | 'fastOutLinearIn' | 'linearOutSlowIn' }`

### `verticalScroll()`

Supported platforms: Android.

Makes the view vertically scrollable. Wraps `Modifier.verticalScroll(rememberScrollState())`. Use on a Column to create a non-lazy scrollable container.

Returns: `ModifierConfig`

### `weight(weight)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `weight` | `number` | Weight value (relative to siblings). |

  

Sets the weight for flexible sizing in Row or Column. Only works when used inside Row or Column.

Returns: `ModifierConfig`

### `width(value)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | Width in dp. |

  

Sets the exact width of the view.

Returns: `ModifierConfig`

### `wrapContentHeight(alignment)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `alignment`(optional) | `'top' | 'bottom' | 'centerVertically'` | Optional vertical alignment ('top', 'centerVertically', 'bottom'). |

  

Wraps the height to the content size.

Returns: `ModifierConfig`

### `wrapContentWidth(alignment)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `alignment`(optional) | `'start' | 'end' | 'centerHorizontally'` | Optional horizontal alignment ('start', 'centerHorizontally', 'end'). |

  

Wraps the width to the content size.

Returns: `ModifierConfig`

### `zIndex(index)`

Supported platforms: Android.

| Parameter | Type | Description |
| --- | --- | --- |
| `index` | `number` | Z-index value. |

  

Sets the z-index for layering.

Returns: `ModifierConfig`

## Event Subscriptions

### `createModifierWithEventListener(type, eventListener, params)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `type` | `string` |
| `eventListener` | `(args: any) => void` |
| `params`(optional) | `Record<string, any>` |

  

Creates a modifier with an event listener.

Returns: `ModifierConfig`

### `createViewModifierEventListener(modifiers)`

Supported platforms: Android.

| Parameter | Type |
| --- | --- |
| `modifiers` | `ModifierConfig[]` |

  

Create an event listener for a view modifier.

Returns: `GlobalEvent`

## Interfaces

### `ModifierConfig`

Supported platforms: Android.

Modifier configuration for native views. This is the JSON Config pattern used by both iOS (SwiftUI) and Android (Jetpack Compose).

| Property | Type | Description |
| --- | --- | --- |
| $scope(optional) | `string` | - |
| $type | `string` | - |

## Types

### `Alignment`

Supported platforms: Android.

Literal Type: `string`

Acceptable values are: `'topStart'` | `'topCenter'` | `'topEnd'` | `'centerStart'` | `'center'` | `'centerEnd'` | `'bottomStart'` | `'bottomCenter'` | `'bottomEnd'` | `'top'` | `'centerVertically'` | `'bottom'` | `'start'` | `'centerHorizontally'` | `'end'`

### `AnimatedValue`

Supported platforms: Android.

Type: `ReturnType<animated>`

### `AnimationSpec`

Supported platforms: Android.

Type: `ReturnType<spring | tween | snap | keyframes>`

### `BuiltinShape`

Supported platforms: Android.

Built-in Jetpack Compose shape for the clip modifier.

Type: `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| type | `'rectangle'` | - |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| type | `'circle'` | - |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| bottomEnd(optional) | `number` | - |
| bottomStart(optional) | `number` | - |
| radius(optional) | `number` | - |
| topEnd(optional) | `number` | - |
| topStart(optional) | `number` | - |
| type | `'roundedCorner'` | - |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| bottomEnd(optional) | `number` | - |
| bottomStart(optional) | `number` | - |
| radius(optional) | `number` | - |
| topEnd(optional) | `number` | - |
| topStart(optional) | `number` | - |
| type | `'cutCorner'` | - |

Or `object` shaped as below:

| Property | Type | Description |
| --- | --- | --- |
| name | `MaterialShapeName` | - |
| type | `'material'` | - |

> **Deprecated:** Use ModifierConfig instead. ExpoModifier (SharedRef pattern) has been replaced with JSON Config pattern for better DX and platform consistency.

### `ExpoModifier`

Supported platforms: Android.

Type: `ModifierConfig`

### `ShadowConfig`

Supported platforms: Android.

Options for the `dropShadow` and `innerShadow` modifiers.

| Property | Type | Description |
| --- | --- | --- |
| alpha(optional) | `number` | Shadow opacity, from 0.0 to 1.0. |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Shadow color string (hex). Defaults to black. |
| offsetX(optional) | `number` | Horizontal offset of the shadow in dp. |
| offsetY(optional) | `number` | Vertical offset of the shadow in dp. |
| radius(optional) | `number` | Blur radius of the shadow in dp. |
| spread(optional) | `number` | Amount to expand (positive) or contract (negative) the shadow geometry in dp. |
