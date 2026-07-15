---
title: "Router Stack - Expo Documentation"
description: "Parsed using standard Python library"
source_url: "https://docs.expo.dev/versions/latest/sdk/router/stack/"
scraped_at: "2026-07-15T08:42:23.366913"
---

[Home](https://docs.expo.dev/)[Guides](https://docs.expo.dev/guides/overview)[EAS](https://docs.expo.dev/eas)[Reference](https://docs.expo.dev/versions/latest)[Learn](https://docs.expo.dev/tutorial/overview)

Reference version

[](https://docs.expo.dev/versions/unversioned)[](https://docs.expo.dev/versions/latest)[](https://docs.expo.dev/versions/v57.0.0)[](https://docs.expo.dev/versions/v56.0.0)[](https://docs.expo.dev/versions/v55.0.0)[](https://docs.expo.dev/versions/v54.0.0)[Archive](https://docs.expo.dev/archive)[Expo Snack](https://snack.expo.dev)[Discord and Forums](https://chat.expo.dev)[Newsletter](https://expo.dev/mailing-list/signup)

This documentation is available as Markdown for AI agents and LLMs. See the[full Markdown index](https://docs.expo.dev/llms.txt)or append .md to any documentation URL.

# Expo Router Stack

An Expo Router API that provides Stack navigator, toolbar, and screen components.

AndroidiOStvOSWebIncluded in Expo Go

[GitHub](https://github.com/expo/expo/tree/sdk-57/packages/expo-router)

[npm](https://www.npmjs.com/package/expo-router)

[Changelog](https://github.com/expo/expo/tree/sdk-57/packages/expo-router/CHANGELOG.md)Recommended version:~57.0.4

An Expo Router API that provides Stack navigator, toolbar, and screen components.

See the [Expo Router](https://docs.expo.dev/versions/latest/sdk/router/index) reference for installation and configuration.

## Usage[](https://docs.expo.dev/versions/latest/sdk/router/stack/#usage)

```
import { Stack } from 'expo-router';

export default function Layout() {
  return <Stack />;
}

```

For more information about using stack navigator, read the stack layout guide:

[Stack layoutLearn how to use the Stack layout in Expo Router.](https://docs.expo.dev/router/advanced/stack)

## API[](https://docs.expo.dev/versions/latest/sdk/router/stack/#api)

```
import { Stack } from 'expo-router';

```

## Components[](https://docs.expo.dev/versions/latest/sdk/router/stack/#components)

### `Stack`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stack)

AndroidiOStvOSWeb

Renders a native stack navigator.

### `Stack.Header`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackheader)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackHeaderProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackheaderprops)>`

The component used to configure header styling for a stack screen.

Use this component to set header appearance properties like blur effect, background color, and shadow visibility.

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Header
        blurEffect="systemMaterial"
        style={{ backgroundColor: '#fff' }}
      />
      <ScreenContent />
    </>
  );
}

```

Example

When used inside a layout with Stack.Screen:

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Header blurEffect="systemMaterial" />
      </Stack.Screen>
    </Stack>
  );
}

```

Note: If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackHeaderProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackheaderprops)

### `asChild`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#aschild)

AndroidiOStvOSWebOptional • Type:`boolean` • Default: `false`

When `true`, renders children as a custom header component, replacing the default header entirely. Use this to implement fully custom header layouts.

### `blurEffect`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#blureffect)

iOSOptional • Type:`[BlurEffect](https://docs.expo.dev/versions/latest/sdk/router/stack/#blureffect)`

The blur effect to apply to the header background on iOS. Common values include 'regular', 'prominent', 'systemMaterial', etc.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children)

AndroidiOStvOSWebOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

Child elements for custom header when `asChild` is true.

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden)

AndroidiOStvOSWebOptional • Type:`boolean` • Default: `false`

Whether to hide the header completely. When set to `true`, the header will not be rendered.

### `largeStyle`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#largestyle)

iOSOptional • Type:`StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent'}>`

Style properties for the large title header (iOS).

- `backgroundColor`: Background color of the large title header- `shadowColor`: Set to 'transparent' to hide the large title shadow/border

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style)

AndroidiOStvOSWebOptional • Type:`StyleProp<{ backgroundColor: [ColorValue](https://reactnative.dev/docs/colors), color: [ColorValue](https://reactnative.dev/docs/colors), shadowColor: 'transparent'}>`

Style properties for the standard-sized header.

- `color`: Tint color for header elements (similar to tintColor in React Navigation)- `backgroundColor`: Background color of the header- `shadowColor`: Set to 'transparent' to hide the header shadow/border

### `transparent`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#transparent)

AndroidiOStvOSWebOptional • Type:`boolean` • Default: `false`

Whether the header should be transparent. When `true`, the header is absolutely positioned and content scrolls underneath.

Auto-enabled when:

- `style.backgroundColor` is 'transparent'- `blurEffect` is set (required for blur to work)

### `Stack.Screen`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreen)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreenprops)>`

StackScreenProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreenprops)

### `dangerouslySingular`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#dangerouslysingular)

AndroidiOStvOSWebOptional • Type:`[SingularOptions](https://docs.expo.dev/versions/v57.0.0/sdk/router#singularoptions)`

When enabled, the navigator will reuse an existing screen instead of pushing a new one.

Only supported when used inside a Layout component.

Deprecated: Use `dangerouslySingular` instead.

Only supported when used inside a Layout component.

### `getId`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#getid)

AndroidiOStvOSWebOptional • Type:`(__namedParameters:{ params: Record<string, any>}) =>string | undefined`

Function to determine a unique ID for the screen.

### `initialParams`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#initialparams)

AndroidiOStvOSWebOptional • Type:`Record<string, any>`

Initial params to pass to the route.

Only supported when used inside a Layout component.

### `listeners`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#listeners)

AndroidiOStvOSWebOptional • Literal type: `union`

Listeners for navigation events.

Only supported when used inside a Layout component.

Acceptable values are:`[Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<{ beforeRemove: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'beforeRemove', true>, blur: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'blur', unknown>, focus: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'focus', unknown>, gestureCancel: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'gestureCancel', unknown>, sheetDetentChange: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'sheetDetentChange', unknown>, state: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'state', unknown>, transitionEnd: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'transitionEnd', unknown>, transitionStart: EventListenerCallback<[NativeStackNavigationEventMap](https://docs.expo.dev/versions/latest/sdk/router/stack/#nativestacknavigationeventmap) & EventMapCore<[StackNavigationState](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacknavigationstate)<ParamListBase>>, 'transitionStart', unknown>}>` | `(prop:{ navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string>}) =>ScreenListeners<TState, TEventMap>`

### `name`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#name)

AndroidiOStvOSWebOptional • Type:`string`

Name is required when used inside a Layout component.

### `options`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#options)

AndroidiOStvOSWebOptional • Literal type: `union`

Options to configure the screen.

Accepts an object or a function returning an object. The function form `options={({ route }) => ({})}` is only supported when used inside a Layout component. When used inside a page component, pass an options object directly.

Acceptable values are:`[NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options)` | `(prop:{ navigation: any, route: [RouteProp](https://reactnavigation.org/docs/glossary-of-terms/#route-object)<ParamListBase, string>}) =>[NativeStackNavigationOptions](https://reactnavigation.org/docs/native-stack-navigator#options)`

### `redirect`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#redirect)

AndroidiOStvOSWebOptional • Type:`boolean`

Redirect to the nearest sibling route. If all children are `redirect={true}`, the layout will render `null` as there are no children to render.

Only supported when used inside a Layout component.

#### Inherited Props[](https://docs.expo.dev/versions/latest/sdk/router/stack/#inherited-props)

- `PropsWithChildren`

### `Stack.SearchBar`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacksearchbar)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackSearchBarProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacksearchbarprops)>`

A search bar component that integrates with the native stack header.

Note: Using `Stack.SearchBar` will automatically make the header visible (`headerShown: true`), as the search bar is rendered as part of the native header.

To display the search bar in the bottom toolbar on iOS 26+, use `Stack.Toolbar.SearchBarSlot` inside `Stack.Toolbar`.

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.SearchBar
        placeholder="Search..."
        onChangeText={(text) => console.log(text)}
      />
     <ScreenContent />
    </>
  );
}

```

StackSearchBarProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacksearchbarprops)

#### Inherited Props[](https://docs.expo.dev/versions/latest/sdk/router/stack/#inherited-props-1)

- `SearchBarProps`

### `Stack.Title`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktitle)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackTitleProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktitleprops)>`

Component to set the screen title.

Can be used inside `Stack.Screen` in a layout or directly inside a screen component.

Example

String title in a layout:

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Title large>Home</Stack.Title>
      </Stack.Screen>
    </Stack>
  );
}

```

Example

String title inside a screen:

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Title>My Page</Stack.Title>
      <ScreenContent />
    </>
  );
}

```

Example

Custom component as the title using `asChild`:

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Title asChild>
          <MyCustomTitle />
        </Stack.Title>
      </Stack.Screen>
    </Stack>
  );
}

```

Note: If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackTitleProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktitleprops)

### `asChild`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#aschild-1)

AndroidiOStvOSWebOptional • Type:`boolean`

Use this to render a custom component as the header title.

Example

```
<Stack.Title asChild>
  <MyCustomTitle />
</Stack.Title>

```

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-1)

AndroidiOStvOSWebOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

The title content. Pass a string for a plain text title, or a custom component when `asChild` is enabled.

### `large`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#large)

iOSOptional • Type:`boolean`

Enables large title mode.

### `largeStyle`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#largestyle-1)

iOSOptional • Type:`StyleProp<{ color: [ColorValue](https://reactnative.dev/docs/colors), fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number>}>`

Style properties for the large title header.

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style-1)

AndroidiOStvOSWebOptional • Type:`StyleProp<{ color: [ColorValue](https://reactnative.dev/docs/colors), fontFamily: TextStyle[fontFamily], fontSize: TextStyle[fontSize], fontWeight: [Exclude](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)<TextStyle[fontWeight], number>, textAlign: 'left' | 'center'}>`

### `Stack.Toolbar`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbar)

Experimental • AndroidiOS

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackToolbarProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarprops)>`

The component used to configure the stack toolbar.

- Use `placement="left"` to customize the left side of the header.- Use `placement="right"` to customize the right side of the header.- Use `placement="bottom"` (default) to show a bottom toolbar.

If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

Note: Using `Stack.Toolbar` with `placement="left"` or `placement="right"` will automatically make the header visible (`headerShown: true`), as the toolbar is rendered as part of the native header.

Note:`Stack.Toolbar` with `placement="bottom"` can only be used inside page components, not in layout components.

Example

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="index">
        <Stack.Toolbar placement="left">
          <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
        </Stack.Toolbar>
        <Stack.Toolbar placement="right">
          <Stack.Toolbar.Button icon="ellipsis.circle" onPress={() => alert('Right button pressed!')} />
        </Stack.Toolbar>
      </Stack.Screen>
    </Stack>
  );
}

```

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="sidebar.left" onPress={() => alert('Left button pressed!')} />
      </Stack.Toolbar>
      <Stack.Toolbar>
        <Stack.Toolbar.Spacer />
        <Stack.Toolbar.Button icon="magnifyingglass" onPress={() => {}} />
        <Stack.Toolbar.Spacer />
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}

```

StackToolbarProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarprops)

### `asChild`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#aschild-2)

AndroidiOSOptional • Type:`boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `backgroundColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#backgroundcolor)

AndroidOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

Background color for the toolbar and its menus.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-2)

AndroidiOSOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom placement, iOS only) components.

### `disableImePadding`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#disableimepadding)

AndroidOptional • Type:`boolean` • Default: `false`

When `true`, disables automatic keyboard (IME) padding on the bottom toolbar.

Only applies to `placement="bottom"` on Android.

### `placement`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#placement)

AndroidiOSOptional • Type:`ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

- `'left'`: Renders items in the left area of the header.- `'right'`: Renders items in the right area of the header.- `'bottom'`: Renders items in the bottom toolbar.

### `tintColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#tintcolor)

AndroidOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

Tint color applied to toolbar items (buttons, menu icons, text). Individual items can override this with their own `tintColor` prop.

### `Stack.Screen.BackButton`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreenbackbutton)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[StackScreenBackButtonProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreenbackbuttonprops)>`

Component to configure the back button.

Can be used inside Stack.Screen in a layout or directly inside a screen component.

Example

```
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <Stack>
      <Stack.Screen name="detail">
        <Stack.Screen.BackButton displayMode="minimal">Back</Stack.Screen.BackButton>
      </Stack.Screen>
    </Stack>
  );
}

```

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Screen.BackButton hidden />
      <ScreenContent />
    </>
  );
}

```

Note: If multiple instances of this component are rendered for the same screen, the last one rendered in the component tree takes precedence.

StackScreenBackButtonProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackscreenbackbuttonprops)

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-3)

AndroidiOStvOSWebOptional • Type:`string`

The title to display for the back button.

### `displayMode`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#displaymode)

iOSOptional • Type:`BackButtonDisplayMode`

The display mode for the back button.

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-1)

AndroidiOStvOSWebOptional • Type:`boolean`

Whether to hide the back button.

### `src`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#src)

AndroidiOStvOSWebOptional • Type:`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)`

Custom image source for the back button.

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style-2)

AndroidiOStvOSWebOptional • Type:`StyleProp<{ fontFamily: string, fontSize: number}>`

Style for the back button title.

### `withMenu`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#withmenu)

iOSOptional • Type:`boolean`

Whether to show a context menu when long pressing the back button.

### `Stack.Toolbar.Badge`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarbadge)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarBadgeProps](https://docs.expo.dev/versions/v57.0.0/sdk/router/stack#stacktoolbarbadgeprops)>>`

StackToolbarBadgeProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarbadgeprops)

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-4)

AndroidiOStvOSWebOptional • Type:`string`

The text to display as the badge

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style-3)

AndroidiOStvOSWebOptional • Type:`StyleProp<[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[TextStyle](https://reactnative.dev/docs/text-style-props), 'fontFamily' | 'fontWeight' | 'color' | 'backgroundColor' | 'fontSize'>>`

### `Stack.Toolbar.Button`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarbutton)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarButtonProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarbuttonprops)>>`

StackToolbarButtonProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarbuttonprops)

### `accessibilityHint`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#accessibilityhint)

iOSOptional • Type:`string`

### `accessibilityLabel`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#accessibilitylabel)

AndroidiOSOptional • Type:`string`

Accessibility label spoken by screen readers (TalkBack/VoiceOver).

See:[Android — Compose accessibility for graphic elements](https://developer.android.com/develop/ui/compose/accessibility/api-defaults#graphic-elements) and [Apple — Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app#Update-your-apps-accessibility) for more information.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-5)

AndroidiOStvOSWebOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

There are two ways to specify the content of the button:

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button icon="star.fill">As text passed as children</Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}

```

Example

```
import { Stack } from 'expo-router';

export default function Page() {
  return (
    <>
      <Stack.Toolbar placement="left">
        <Stack.Toolbar.Button>
          <Stack.Toolbar.Icon sf="star.fill" />
          <Stack.Toolbar.Label>As components</Stack.Toolbar.Label>
          <Stack.Toolbar.Badge>3</Stack.Toolbar.Badge>
        </Stack.Toolbar.Button>
      </Stack.Toolbar>
      <ScreenContent />
    </>
  );
}

```

Note: When icon is used, the label will not be shown and will be used for accessibility purposes only. Badge is only supported in left/right placements, not in bottom (iOS toolbar limitation).

### `disabled`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#disabled)

AndroidiOSOptional • Type:`boolean`

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-2)

AndroidiOSOptional • Type:`boolean` • Default: `false`

Whether the button should be hidden.

### `hidesSharedBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidessharedbackground)

iOS 26+Optional • Type:`boolean`

Whether to hide the shared background.

### `icon`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#icon)

AndroidiOSOptional • Literal type: `union`

Icon to display in the button.

On Android, only image source is supported.

On iOS, it can be a string representing an SFSymbol, an image source or xcasset.

Note: When used in `placement="bottom"` on iOS, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Acceptable values are:`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)` | `[SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)`

### `iconRenderingMode`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#iconrenderingmode)

AndroidiOSOptional • Literal type: `string`

Controls how image-based icons are rendered.

- `'template'`: applies tint color to the icon- `'original'`: preserves original icon colors (useful for multi-color icons)

Default behavior on iOS:

- If `tintColor` is specified, defaults to `'template'`- If no `tintColor`, defaults to `'original'`

On Android: defaults to `'template'`.

This prop only affects image-based icons (not SF Symbols).

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are:`'template'` | `'original'`

### `image`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#image)

iOSOptional • Literal type: `union`

Image to display in the button.

Note: This prop is only supported in toolbar with `placement="bottom"`.

Acceptable values are:`[SharedRef](https://docs.expo.dev/versions/v57.0.0/sdk/expo#sharedreftype)<'image', Record<never, never>>` | `null`

### `onPress`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#onpress)

AndroidiOStvOSWebOptional • Type:`() =>void`

### `selected`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#selected)

iOSOptional • Type:`boolean`

Whether the button is in a selected state

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/isselected) for more information

### `separateBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#separatebackground)

iOSOptional • Type:`boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style-4)

AndroidiOSOptional • Type:`StyleProp<[TextStyle](https://reactnative.dev/docs/text-style-props)>`

Style for the label of the header item.

### `tintColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#tintcolor-1)

AndroidiOSOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

The tint color to apply to the button item.

See: - [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

- [Android documentation](https://developer.android.com/develop/ui/compose/graphics/images/customize#tint-image) for more information.

### `variant`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#variant)

iOSOptional • Literal type: `string` • Default: `'plain'`

Acceptable values are:`'done'` | `'plain'` | `'prominent'`

### `Stack.Toolbar.Icon`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbaricon)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarIconProps](https://docs.expo.dev/versions/v57.0.0/sdk/router/stack#stacktoolbariconprops)>>`

StackToolbarIconProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbariconprops)

### `renderingMode`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#renderingmode)

AndroidiOSOptional • Literal type: `string`

Controls how the image icon is rendered.

- `'template'`: applies tint color to the icon- `'original'`: preserves original icon colors

Default behavior on iOS:

- With parent `tintColor`: defaults to `'template'`- Without parent `tintColor`: defaults to `'original'`

On Android: defaults to `'template'`. Setting `'original'` skips the tint so the icon's source colors are preserved.

Acceptable values are:`'template'` | `'original'`

### `src`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#src-1)

AndroidiOStvOSWebType:`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)`

### `sf`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#sf)

iOSType:`[SFSymbol](https://github.com/nandorojo/sf-symbols-typescript)`

Name of an SF Symbol to display.

### `xcasset`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#xcasset)

iOSType:`string`

Name of an image in your Xcode asset catalog (`.xcassets`).

### `Stack.Toolbar.Label`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarlabel)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarLabelProps](https://docs.expo.dev/versions/v57.0.0/sdk/router/stack#stacktoolbarlabelprops)>>`

StackToolbarLabelProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarlabelprops)

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-6)

AndroidiOStvOSWebOptional • Type:`string`

The text to display as the label for the tab.

### `Stack.Toolbar.Menu`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenu)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenuprops)>>`

StackToolbarMenuProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenuprops)

### `accessibilityHint`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#accessibilityhint-1)

iOSOptional • Type:`string`

### `accessibilityLabel`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#accessibilitylabel-1)

AndroidiOSOptional • Type:`string`

Accessibility label spoken by screen readers (TalkBack/VoiceOver).

See:[Android — Compose accessibility for graphic elements](https://developer.android.com/develop/ui/compose/accessibility/api-defaults#graphic-elements) and [Apple — Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app#Update-your-apps-accessibility) for more information.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-7)

AndroidiOSOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

Menu content - can include icons, labels, badges and menu actions.

Example

```
<Stack.Toolbar.Menu>
  <Stack.Toolbar.Icon sfSymbol="ellipsis.circle" />
  <Stack.Toolbar.Label>Options</Stack.Toolbar.Label>
  <Stack.Toolbar.MenuAction onPress={() => {}}>Action 1</Stack.Toolbar.MenuAction>
</Stack.Toolbar.Menu>

```

### `destructive`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#destructive)

iOSOptional • Type:`boolean`

If `true`, the menu item will be displayed as destructive.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#disabled-1)

AndroidiOSOptional • Type:`boolean`

### `elementSize`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#elementsize)

iOS 16.0+Optional • Literal type: `string`

The preferred size of the menu elements.

Note: This prop is only supported in `Stack.Toolbar.Bottom`.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize) for more information.

Acceptable values are:`'small'` | `'medium'` | `'auto'` | `'large'`

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-3)

AndroidiOSOptional • Type:`boolean` • Default: `false`

Whether the menu should be hidden.

### `hidesSharedBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidessharedbackground-1)

iOS 26+Optional • Type:`boolean`

Whether to hide the shared background.

See:[Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `icon`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#icon-1)

AndroidiOSOptional • Literal type: `union`

Icon for the menu item.

Can be an SF Symbol name or an image source.

Note: When used in `placement="bottom"` on iOS, only string SFSymbols are supported. Use the `image` prop to provide custom images.

Note (Android): Only `ImageSourcePropType` icons are rendered at the menu root. SF Symbols and `xcasset` names are silently dropped — provide a `require()` or `{ uri }` source.

Acceptable values are:`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)` | `[SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)`

### `iconRenderingMode`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#iconrenderingmode-1)

AndroidiOSOptional • Literal type: `string`

Controls how image-based icons are rendered.

- `'template'`: applies tint color to the icon (useful for monochrome icons)- `'original'`: preserves original icon colors (useful for multi-color icons)

Default behavior on iOS:

- If `tintColor` is specified, defaults to `'template'`- If no `tintColor`, defaults to `'original'`

On Android: defaults to `'template'`.

This prop only affects image-based icons (not SF Symbols).

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are:`'template'` | `'original'`

### `image`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#image-1)

iOSOptional • Literal type: `union`

Image to display for the menu item.

Note: This prop is only supported in toolbar with `placement="bottom"`.

Acceptable values are:`[SharedRef](https://docs.expo.dev/versions/v57.0.0/sdk/expo#sharedreftype)<'image', Record<never, never>>` | `null`

### `inline`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#inline)

AndroidiOSOptional • Type:`boolean`

If `true`, the menu will be displayed inline. This means that the menu will not be collapsed.

Note: Inline menus are only supported in submenus.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayinline) for more information.

### `palette`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#palette)

iOSOptional • Type:`boolean`

If `true`, the menu will be displayed as a palette. This means that the menu will be displayed as one row.

Note: Palette menus are only supported in submenus.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct/displayaspalette) for more information.

### `separateBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#separatebackground-1)

iOSOptional • Type:`boolean` • Default: `false`

Whether to separate the background of this item from other header items.

### `style`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#style-5)

AndroidiOSOptional • Type:`StyleProp<BasicTextStyle>`

Style for the label of the header item.

### `tintColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#tintcolor-2)

AndroidiOSOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

The tint color to apply to the button item.

See: - [Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor) for more information.

- [Android documentation](https://developer.android.com/develop/ui/compose/graphics/images/customize#tint-image) for more information.

### `title`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#title)

AndroidiOSOptional • Type:`string`

Optional title to show on top of the menu.

### `variant`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#variant-1)

iOSOptional • Literal type: `string` • Default: `'plain'`

Acceptable values are:`'done'` | `'plain'` | `'prominent'`

### `Stack.Toolbar.MenuAction`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenuaction)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarMenuActionProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenuactionprops)>>`

StackToolbarMenuActionProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarmenuactionprops)

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-8)

AndroidiOStvOSWebOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

Can be an Icon, Label or string title.

### `destructive`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#destructive-1)

AndroidiOSOptional • Type:`boolean`

If `true`, the menu item will be displayed as destructive.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/destructive) for more information.

### `disabled`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#disabled-2)

AndroidiOStvOSWebOptional • Type:`boolean`

If `true`, the menu item will be disabled and not selectable.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/disabled) for more information.

### `discoverabilityLabel`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#discoverabilitylabel)

iOSOptional • Type:`string`

An elaborated title that explains the purpose of the action.

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-4)

AndroidiOStvOSWebOptional • Type:`boolean`

### `icon`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#icon-2)

AndroidiOStvOSWebOptional • Literal type: `union`

Icon for the menu action.

Can be an SF Symbol name or an image source.

Note (Android): Only `ImageSourcePropType` icons are rendered. SF Symbols are silently dropped. Provide a `require()` or `{ uri }` source.

Acceptable values are:`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource)` | `[SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)`

### `iconRenderingMode`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#iconrenderingmode-2)

iOSOptional • Literal type: `string`

Controls how image-based icons are rendered on iOS.

- `'template'`: iOS applies tint color to the icon (useful for monochrome icons)- `'original'`: Preserves original icon colors (useful for multi-color icons)

Default behavior:

- If `tintColor` is specified, defaults to `'template'`- If no `tintColor`, defaults to `'original'`

This prop only affects image-based icons (not SF Symbols).

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

Acceptable values are:`'template'` | `'original'`

### `image`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#image-2)

iOSOptional • Literal type: `union`

Image to display for the menu action.

Note: This prop is only supported in `Stack.Toolbar.Bottom`.

Acceptable values are:`[SharedRef](https://docs.expo.dev/versions/v57.0.0/sdk/expo#sharedreftype)<'image', Record<never, never>>` | `null`

### `isOn`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#ison)

AndroidiOSOptional • Type:`boolean`

If `true`, the menu item will be displayed as selected.

### `onPress`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#onpress-1)

AndroidiOStvOSWebOptional • Type:`() =>void`

### `subtitle`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#subtitle)

iOSOptional • Type:`string`

An optional subtitle for the menu item.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/subtitle) for more information.

### `unstable_keepPresented`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#unstable_keeppresented)

AndroidiOSOptional • Type:`boolean`

If `true`, the menu will be kept presented after the action is selected.

This is marked as unstable, because when action is selected on iOS it will recreate the menu, which will close all opened submenus and reset the scroll position.

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uimenuelement/attributes/keepsmenupresented) for more information.

### `Stack.Toolbar.SearchBarSlot`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarsearchbarslot)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSearchBarSlotProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarsearchbarslotprops)>>`

StackToolbarSearchBarSlotProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarsearchbarslotprops)

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-5)

AndroidiOStvOSWebOptional • Type:`boolean` • Default: `false`

Whether the search bar slot should be hidden.

### `hidesSharedBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidessharedbackground-2)

iOS 26+Optional • Type:`boolean`

Whether to hide the shared background.

### `separateBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#separatebackground-2)

iOS 26+Optional • Type:`boolean`

Whether this search bar slot has a separate background from adjacent items. When this prop is `true`, the search bar will always render as `integratedButton`.

In order to render the search bar with a separate background, ensure that adjacent toolbar items have `separateBackground` set to `true` or use `Stack.Toolbar.Spacer` to create spacing.

Example

```
<Stack.SearchBar onChangeText={()=>{}} />
<Stack.Toolbar placement="bottom">
  <Stack.Toolbar.SearchBarSlot />
  <Stack.Toolbar.Spacer />
  <Stack.Toolbar.Button icon="square.and.pencil" />
</Stack.Toolbar>

```

### `Stack.Toolbar.Spacer`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarspacer)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarSpacerProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarspacerprops)>>`

StackToolbarSpacerProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarspacerprops)

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-6)

AndroidiOSOptional • Type:`boolean` • Default: `false`

Whether the spacer should be hidden.

### `sharesBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#sharesbackground)

iOS 26+Optional • Type:`boolean`

Whether this spacer shares background with adjacent items.

Only available in bottom placement.

### `width`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#width)

AndroidiOSOptional • Type:`number`

The width of the spacing element.

In Left/Right placements, width is required. In Bottom placement, if width is not provided, the spacer will be flexible and expand to fill available space.

Note: On Android, `width` is required in every placement.

### `Stack.Toolbar.View`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarview)

AndroidiOStvOSWeb

Type:`React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[StackToolbarViewProps](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarviewprops)>>`

StackToolbarViewProps[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stacktoolbarviewprops)

### `asChild`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#aschild-3)

AndroidiOSOptional • Type:`boolean` • Default: `false`

When `true`, renders children as a custom component in the header area, replacing the default header layout.

Only applies to `placement="left"` and `placement="right"`.

### `backgroundColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#backgroundcolor-1)

AndroidOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

Background color for the toolbar and its menus.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-9)

AndroidiOSOptional • Type:`[ReactNode](https://reactnative.dev/docs/react-node)`

Child elements to compose the toolbar. Can include Stack.Toolbar.Button, Stack.Toolbar.Menu, Stack.Toolbar.View, Stack.Toolbar.Spacer, and Stack.Toolbar.SearchBarSlot (bottom placement, iOS only) components.

### `disableImePadding`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#disableimepadding-1)

AndroidOptional • Type:`boolean` • Default: `false`

When `true`, disables automatic keyboard (IME) padding on the bottom toolbar.

Only applies to `placement="bottom"` on Android.

### `placement`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#placement-1)

AndroidiOSOptional • Type:`ToolbarPlacement` • Default: `'bottom'`

The placement of the toolbar.

- `'left'`: Renders items in the left area of the header.- `'right'`: Renders items in the right area of the header.- `'bottom'`: Renders items in the bottom toolbar.

### `tintColor`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#tintcolor-3)

AndroidOptional • Type:`[ColorValue](https://reactnative.dev/docs/colors)`

Tint color applied to toolbar items (buttons, menu icons, text). Individual items can override this with their own `tintColor` prop.

### `children`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#children-10)

AndroidiOSOptional • Type:`ReactElement<unknown, string | JSXElementConstructor<any>>`

Can be any React node.

### `hidden`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidden-7)

AndroidiOSOptional • Type:`boolean` • Default: `false`

Whether the view should be hidden.

### `hidesSharedBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#hidessharedbackground-3)

iOS 26+Optional • Type:`boolean`

Whether to hide the shared background.

See:[Official Apple documentation](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground) for more information.

### `separateBackground`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#separatebackground-3)

iOSOptional • Type:`boolean` • Default: `false`

Whether to separate the background of this item from other items.

Only available in bottom placement.

## Interfaces[](https://docs.expo.dev/versions/latest/sdk/router/stack/#interfaces)

### `StackHeaderItemSharedProps`[](https://docs.expo.dev/versions/latest/sdk/router/stack/#stackheaderitemsharedprops)

AndroidiOStvOSWebPropertyTypeDescriptionaccessibilityHint(optional)`string`-accessibilityLabel(optional)`string`-children(optional)`[ReactNode](https://reactnative.dev/docs/react-node)`-disabled(optional)`boolean`-hidesSharedBackground(optional)`boolean`-icon(optional)`[ImageSourcePropType](https://reactnative.dev/docs/image#imagesource) | [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)`-iconRenderingMode(optional)`'template' | 'original'`Only for:AndroidiOS

Controls how image-based icons are rendered.

- `'template'`: applies tint color to the icon- `'original'`: preserves original icon colors (useful for multi-color icons)

Default behavior on iOS:

- If `tintColor` is specified, defaults to `'template'`- If no `tintColor`, defaults to `'original'`

On Android: defaults to `'template'`. The icon is always rendered through Compose's `Icon` and tinted unless `'original'` is set explicitly.

This prop only affects image-based icons (not SF Symbols).

See:[Apple documentation](https://developer.apple.com/documentation/uikit/uiimage/renderingmode-swift.enum) for more information.

separateBackground(optional)`boolean`-style(optional)`StyleProp<BasicTextStyle>`-tintColor(optional)`[ColorValue](https://reactnative.dev/docs/colors)`-variant(optional)`'done' | 'plain' | 'prominent'`Default:`'plain'`